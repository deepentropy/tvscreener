/**
 * Code Generator for tvscreener
 * Generates Python code from UI configuration
 */

const CodeGenerator = {
    /**
     * Generate complete Python code from configuration
     * @param {Object} config - Configuration object
     * @returns {string} Generated Python code
     */
    generate(config) {
        return this.generateLines(config).map(l => l.text).join('\n');
    },

    /**
     * Generate code lines tagged with the UI section that produced them
     * @param {Object} config - Configuration object
     * @returns {Array<{text: string, section: string|null}>}
     */
    generateLines(config) {
        const lines = [];
        const add = (section, text) => {
            for (const t of text.split('\n')) lines.push({ text: t, section });
        };
        const blank = () => lines.push({ text: '', section: null });

        for (const imp of this.generateImports(config)) add('screener', imp);
        blank();
        add('screener', this.generateScreenerCreation(config));

        // Filters: rows joined by OR become one where() call, groups are ANDed
        const filterLines = this.generateFilterLines(config);
        if (filterLines.length > 0) {
            blank();
            add('filters', '# Filters');
            for (const line of filterLines) add('filters', line);
        }

        // Fields
        if (config.selectAll) {
            blank();
            add('fields', '# Select all available fields');
            add('fields', 'ss.select_all()');
        } else if (config.fields && config.fields.length > 0) {
            blank();
            add('fields', '# Fields to retrieve');
            add('fields', this.generateSelect(config.fields, config));
        }

        // Markets (only for stock screener)
        if (this.hasMarkets(config)) {
            blank();
            add('options', '# Markets');
            add('options', this.generateMarkets(config));
        }

        // Index (only for stock screener)
        if (config.index && config.screenerConfig?.hasIndex) {
            blank();
            add('options', '# Filter by index');
            add('options', `ss.set_index(IndexSymbol.${config.index})`);
        }

        // Sort
        if (config.sortField) {
            blank();
            add('options', '# Sorting');
            const ascending = config.sortOrder === 'asc' ? 'True' : 'False';
            const sortRef = this.fieldRef(config.sortField, config.sortInterval, config);
            add('options', `ss.sort_by(${sortRef}, ascending=${ascending})`);
        }

        // Limit
        if (config.limit && config.limit !== 150) {
            blank();
            add('options', '# Result limit');
            add('options', `ss.set_range(0, ${config.limit})`);
        }

        // Get data
        blank();
        add('run', '# Execute query');
        add('run', 'df = ss.get()');
        add('run', 'print(f"Found {len(df)} results")');
        add('run', 'df.head(20)');

        return lines;
    },

    /**
     * Generate import statements
     */
    generateImports(config) {
        const items = [];
        const screenerClass = config.screenerConfig?.class || 'StockScreener';
        const fieldClass = config.screenerConfig?.fieldClass || 'StockField';

        // Screener class
        items.push(screenerClass);

        // Field class (if used for fields, filters, or sorting)
        const needsFieldClass =
            (config.fields && config.fields.length > 0) ||
            (config.filters && config.filters.length > 0) ||
            config.sortField ||
            config.selectAll;

        if (needsFieldClass) {
            items.push(fieldClass);
        }

        // IndexSymbol if used
        if (config.index && config.screenerConfig?.hasIndex) {
            items.push('IndexSymbol');
        }

        // Market if used
        if (this.hasMarkets(config)) {
            items.push('Market');
        }

        return [`from tvscreener import ${items.join(', ')}`];
    },

    /**
     * Python reference to a field, with its time interval when one is set
     * and the field supports it
     */
    fieldRef(name, interval, config) {
        const fieldClass = config.screenerConfig?.fieldClass || 'StockField';
        const ref = `${fieldClass}.${name}`;
        return interval && this.supportsInterval(name, config)
            ? `${ref}.with_interval('${interval}')`
            : ref;
    },

    supportsInterval(name, config) {
        const fields = config.screenerConfig?.fields || [];
        return !!fields.find(f => f.name === name)?.interval;
    },

    hasMarkets(config) {
        return !!(config.markets && config.markets.length > 0 && config.screenerConfig?.hasMarket);
    },

    /**
     * Generate set_markets line; Market.ALL replaces any other market
     */
    generateMarkets(config) {
        const names = config.markets.includes('ALL') ? ['ALL'] : config.markets;
        return `ss.set_markets(${names.map(n => `Market.${n}`).join(', ')})`;
    },

    /**
     * Generate screener creation line
     */
    generateScreenerCreation(config) {
        const screenerClass = config.screenerConfig?.class || 'StockScreener';
        return `ss = ${screenerClass}()`;
    },

    // Operators by the inputs they need
    COMPARISONS: ['>', '>=', '<', '<=', '==', '!='],
    NO_VALUE_OPERATORS: ['is_empty', 'not_empty'],
    TWO_VALUE_OPERATORS: ['between', 'in_day_range', 'within_pct', 'not_within_pct'],
    NUMERIC_OPERATORS: ['in_day_range', 'above_pct', 'below_pct', 'within_pct', 'not_within_pct'],
    REFERENCE_OPERATORS: ['above_pct', 'below_pct', 'within_pct', 'not_within_pct'],
    LIST_OPERATORS: ['isin', 'not_in', 'has', 'has_none_of'],

    /**
     * Check that a filter has every input its operator needs
     */
    isComplete(filter) {
        if (!filter.field || !filter.operator) return false;
        const op = filter.operator;
        if (this.NO_VALUE_OPERATORS.includes(op)) return true;
        if (this.REFERENCE_OPERATORS.includes(op) && !filter.ref) return false;
        const values = this.TWO_VALUE_OPERATORS.includes(op) ? [filter.value, filter.value2] : [filter.value];
        if (values.some(v => v === undefined || String(v).trim() === '')) return false;
        if (this.NUMERIC_OPERATORS.includes(op)) return values.every(v => !isNaN(Number(v)));
        return true;
    },

    /**
     * Python expression of one filter condition
     * @returns {{expr: string, comparison: boolean}|null} comparison is true when the
     *          expression needs parentheses to be combined with | or &
     */
    generateCondition(filter, config) {
        if (!this.isComplete(filter)) return null;

        const ref = this.fieldRef(filter.field, filter.interval, config);
        const op = filter.operator;
        const value = () => this.formatValue(filter.value, filter.format);
        const number = (v) => String(Number(v));
        const list = () => filter.value.split(',').map(v => this.formatValue(v.trim(), filter.format));

        if (this.COMPARISONS.includes(op)) {
            return { expr: `${ref} ${op} ${value()}`, comparison: true };
        }

        const call = (text) => ({ expr: `${ref}.${text}`, comparison: false });
        const other = () => this.fieldRef(filter.ref, '', config);
        switch (op) {
            case 'between':
                return call(`between(${value()}, ${this.formatValue(filter.value2, filter.format)})`);
            case 'isin':
            case 'not_in':
                return call(`${op}([${list().join(', ')}])`);
            case 'has':
            case 'has_none_of': {
                const values = list();
                return call(`${op}(${values.length === 1 ? values[0] : `[${values.join(', ')}]`})`);
            }
            case 'is_empty':
            case 'not_empty':
                return call(`${op}()`);
            case 'in_day_range':
                return call(`in_day_range(${number(filter.value)}, ${number(filter.value2)})`);
            case 'above_pct':
            case 'below_pct':
                return call(`${op}(${other()}, ${number(filter.value)})`);
            case 'within_pct':
            case 'not_within_pct':
                return call(`${op}(${other()}, ${number(filter.value)}, ${number(filter.value2)})`);
            default:
                return null;
        }
    },

    /**
     * Generate the where() lines. A filter joined with OR to the previous one
     * joins its group; each group becomes one where() call.
     */
    generateFilterLines(config) {
        const groups = [];
        for (const filter of config.filters || []) {
            const condition = this.generateCondition(filter, config);
            if (!condition) continue;
            if (filter.join === 'or' && groups.length > 0) {
                groups[groups.length - 1].push(condition);
            } else {
                groups.push([condition]);
            }
        }

        const lines = [];
        for (const group of groups) {
            if (group.length === 1) {
                lines.push(`ss.where(${group[0].expr})`);
                continue;
            }
            const parts = group.map(c => (c.comparison ? `(${c.expr})` : c.expr));
            const oneLine = `ss.where(${parts.join(' | ')})`;
            if (oneLine.length <= 88) {
                lines.push(oneLine);
            } else {
                lines.push('ss.where(');
                parts.forEach((part, i) => lines.push(`    ${i === 0 ? '' : '| '}${part}`));
                lines.push(')');
            }
        }
        return lines;
    },

    /**
     * Format a value based on its type
     */
    formatValue(value, format) {
        if (value === null || value === undefined || value === '') {
            return 'None';
        }

        // Check if it's a number
        const num = parseFloat(value);
        if (!isNaN(num) && format !== 'text') {
            // Format large numbers with underscores for readability
            if (Math.abs(num) >= 1000000) {
                return this.formatLargeNumber(num);
            }
            return String(num);
        }

        // String value - escape backslashes first, then quotes
        return `'${value.replace(/\\/g, '\\\\').replace(/'/g, "\\'")}'`;
    },

    /**
     * Format large numbers with underscores
     */
    formatLargeNumber(num) {
        if (num >= 1e12) {
            return `${num / 1e12}e12`;
        } else if (num >= 1e9) {
            const billions = num / 1e9;
            if (Number.isInteger(billions)) {
                return `${billions}e9`;
            }
            return `${billions}e9`;
        } else if (num >= 1e6) {
            const millions = num / 1e6;
            if (Number.isInteger(millions)) {
                return `${millions}_000_000`;
            }
            return String(num).replace(/\B(?=(\d{3})+(?!\d))/g, '_');
        }
        return String(num).replace(/\B(?=(\d{3})+(?!\d))/g, '_');
    },

    /**
     * Generate select statement
     */
    generateSelect(fields, config) {
        if (fields.length === 0) {
            return '# Using default fields';
        }

        const refs = fields.map(f => this.fieldRef(f, config.fieldsInterval, config));

        if (refs.length <= 3) {
            return `ss.select(${refs.join(', ')})`;
        }

        // Multi-line for many fields
        const lines = ['ss.select('];
        for (let i = 0; i < refs.length; i++) {
            const comma = i < refs.length - 1 ? ',' : '';
            lines.push(`    ${refs[i]}${comma}`);
        }
        lines.push(')');
        return lines.join('\n');
    }
};

// Export for use in app.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CodeGenerator;
}
