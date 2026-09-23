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

        // Filters
        if (config.filters && config.filters.length > 0) {
            blank();
            add('filters', '# Filters');
            for (const filter of config.filters) {
                const filterLine = this.generateFilter(filter, config);
                if (filterLine) {
                    add('filters', filterLine);
                }
            }
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

    /**
     * Generate a single filter line
     */
    generateFilter(filter, config) {
        if (!filter.field || !filter.operator || filter.value === '') {
            return null;
        }

        const fieldRef = this.fieldRef(filter.field, filter.interval, config);

        switch (filter.operator) {
            case '>':
                return `ss.where(${fieldRef} > ${this.formatValue(filter.value, filter.format)})`;
            case '>=':
                return `ss.where(${fieldRef} >= ${this.formatValue(filter.value, filter.format)})`;
            case '<':
                return `ss.where(${fieldRef} < ${this.formatValue(filter.value, filter.format)})`;
            case '<=':
                return `ss.where(${fieldRef} <= ${this.formatValue(filter.value, filter.format)})`;
            case '==':
                return `ss.where(${fieldRef} == ${this.formatValue(filter.value, filter.format)})`;
            case '!=':
                return `ss.where(${fieldRef} != ${this.formatValue(filter.value, filter.format)})`;
            case 'between':
                return `ss.where(${fieldRef}.between(${this.formatValue(filter.value, filter.format)}, ${this.formatValue(filter.value2, filter.format)}))`;
            case 'isin':
            case 'not_in': {
                const values = filter.value.split(',').map(v => this.formatValue(v.trim(), filter.format));
                return `ss.where(${fieldRef}.${filter.operator}([${values.join(', ')}]))`;
            }
            default:
                return null;
        }
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
