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
        lines.push(this.generateScreenerCreation(config.screenerType));

        // Filters
        if (config.filters && config.filters.length > 0) {
            lines.push('');
            lines.push('# Filters');
            for (const filter of config.filters) {
                const filterLine = this.generateFilter(filter, config.screenerType);
                if (filterLine) {
                    lines.push(filterLine);
                }
            }
        }

        // Fields
        if (config.fields && config.fields.length > 0) {
            lines.push('');
            lines.push('# Fields to retrieve');
            lines.push(this.generateSelect(config.fields, config.screenerType));
        }

        // Index
        if (config.index) {
            lines.push('');
            lines.push('# Filter by index');
            lines.push(`ss.set_index(IndexSymbol.${config.index})`);
        }

        // Sort
        if (config.sortField) {
            lines.push('');
            lines.push('# Sorting');
            const ascending = config.sortOrder === 'asc' ? 'True' : 'False';
            lines.push(`ss.sort_by(${this.getFieldClass(config.screenerType)}.${config.sortField}, ascending=${ascending})`);
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
        const imports = ['from tvscreener import'];
        const items = [];

        // Screener class
        items.push(this.getScreenerClass(config.screenerType));

        // Field class
        items.push(this.getFieldClass(config.screenerType));

        // IndexSymbol if used
        if (config.index) {
            items.push('IndexSymbol');
        }

        return [`from tvscreener import ${items.join(', ')}`];
    },

    /**
     * Get screener class name
     */
    getScreenerClass(type) {
        const classes = {
            stock: 'StockScreener',
            crypto: 'CryptoScreener',
            forex: 'ForexScreener'
        };
        return classes[type] || 'StockScreener';
    },

    /**
     * Get field class name
     */
    getFieldClass(type) {
        const classes = {
            stock: 'StockField',
            crypto: 'CryptoField',
            forex: 'ForexField'
        };
        return classes[type] || 'StockField';
    },

    /**
     * Generate screener creation line
     */
    generateScreenerCreation(type) {
        return `ss = ${this.getScreenerClass(type)}()`;
    },

    /**
     * Generate a single filter line
     */
    generateFilter(filter, screenerType) {
        if (!filter.field || !filter.operator || filter.value === '') {
            return null;
        }

        const fieldClass = this.getFieldClass(screenerType);
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
    generateSelect(fields, screenerType) {
        if (fields.length === 0) {
            return '# Using default fields';
        }

        const fieldClass = this.getFieldClass(screenerType);

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
