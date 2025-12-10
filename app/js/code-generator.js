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
        const lines = [];
        const imports = this.generateImports(config);

        lines.push(...imports);
        lines.push('');
        lines.push(this.generateScreenerCreation(config));

        // Filters
        if (config.filters && config.filters.length > 0) {
            lines.push('');
            lines.push('# Filters');
            for (const filter of config.filters) {
                const filterLine = this.generateFilter(filter, config);
                if (filterLine) {
                    lines.push(filterLine);
                }
            }
        }

        // Fields
        if (config.selectAll) {
            lines.push('');
            lines.push('# Select all available fields');
            lines.push('ss.select_all()');
        } else if (config.fields && config.fields.length > 0) {
            lines.push('');
            lines.push('# Fields to retrieve');
            lines.push(this.generateSelect(config.fields, config));
        }

        // Index (only for stock screener)
        if (config.index && config.screenerConfig?.hasIndex) {
            lines.push('');
            lines.push('# Filter by index');
            lines.push(`ss.set_index(IndexSymbol.${config.index})`);
        }

        // Sort
        if (config.sortField) {
            lines.push('');
            lines.push('# Sorting');
            const ascending = config.sortOrder === 'asc' ? 'True' : 'False';
            const fieldClass = config.screenerConfig?.fieldClass || 'StockField';
            lines.push(`ss.sort_by(${fieldClass}.${config.sortField}, ascending=${ascending})`);
        }

        // Limit
        if (config.limit && config.limit !== 150) {
            lines.push('');
            lines.push('# Result limit');
            lines.push(`ss.set_range(0, ${config.limit})`);
        }

        // Get data
        lines.push('');
        lines.push('# Execute query');
        lines.push('df = ss.get()');
        lines.push('print(f"Found {len(df)} results")');
        lines.push('df.head(20)');

        return lines.join('\n');
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

        return [`from tvscreener import ${items.join(', ')}`];
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

        const fieldClass = config.screenerConfig?.fieldClass || 'StockField';
        const fieldRef = `${fieldClass}.${filter.field}`;

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
                const values = filter.value.split(',').map(v => this.formatValue(v.trim(), filter.format));
                return `ss.where(${fieldRef}.isin([${values.join(', ')}]))`;
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

        // String value
        return `'${value.replace(/'/g, "\\'")}'`;
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

        const fieldClass = config.screenerConfig?.fieldClass || 'StockField';

        if (fields.length <= 3) {
            const fieldRefs = fields.map(f => `${fieldClass}.${f}`).join(', ');
            return `ss.select(${fieldRefs})`;
        }

        // Multi-line for many fields
        const lines = ['ss.select('];
        for (let i = 0; i < fields.length; i++) {
            const comma = i < fields.length - 1 ? ',' : '';
            lines.push(`    ${fieldClass}.${fields[i]}${comma}`);
        }
        lines.push(')');
        return lines.join('\n');
    }
};

// Export for use in app.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CodeGenerator;
}
