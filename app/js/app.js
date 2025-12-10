/**
 * tvscreener Code Generator - Main Application
 */

const App = {
    // State
    state: {
        screenerType: 'stock',
        filters: [],
        selectedFields: [],
        selectAll: false,
        index: '',
        sortField: '',
        sortOrder: 'desc',
        limit: 100
    },

    // DOM Elements
    elements: {},

    // Field presets per screener type
    presets: {
        stock: {
            basic: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'VOLUME', 'MARKET_CAPITALIZATION'],
            valuation: ['NAME', 'PRICE', 'PE_RATIO_TTM', 'PRICE_TO_BOOK_FY', 'PRICE_TO_SALES_FY', 'EV_TO_EBITDA_TTM', 'MARKET_CAPITALIZATION'],
            technical: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'RELATIVE_STRENGTH_INDEX_14', 'MACD_LEVEL_12_26', 'SIMPLE_MOVING_AVERAGE_50', 'SIMPLE_MOVING_AVERAGE_200'],
            performance: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'PERFORMANCE_1_WEEK', 'PERFORMANCE_1_MONTH', 'PERFORMANCE_3_MONTH', 'PERFORMANCE_YEAR_TO_DATE'],
            dividends: ['NAME', 'PRICE', 'DIVIDEND_YIELD_FY', 'DIVIDENDS_PER_SHARE_FY', 'PAYOUT_RATIO_TTM']
        },
        crypto: {
            basic: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'VOLUME', 'MARKET_CAPITALIZATION'],
            technical: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'RELATIVE_STRENGTH_INDEX_14', 'MACD_LEVEL_12_26'],
            performance: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'PERFORMANCE_1_WEEK', 'PERFORMANCE_1_MONTH']
        },
        forex: {
            basic: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'BID', 'ASK'],
            technical: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'RELATIVE_STRENGTH_INDEX_14', 'MACD_LEVEL_12_26']
        },
        bond: {
            basic: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'YIELD']
        },
        futures: {
            basic: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'VOLUME']
        },
        coin: {
            basic: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'VOLUME', 'MARKET_CAPITALIZATION']
        }
    },

    /**
     * Get current screener config from FIELD_DATA
     */
    getScreenerConfig() {
        return FIELD_DATA.screeners[this.state.screenerType];
    },

    /**
     * Get fields for current screener
     */
    getFields() {
        return this.getScreenerConfig()?.fields || [];
    },

    /**
     * Initialize the application
     */
    init() {
        this.cacheElements();
        this.populateIndices();
        this.populateCategories();
        this.populateSortFields();
        this.renderFields();
        this.bindEvents();
        this.updateCode();
        this.updateFieldCounter();
    },

    /**
     * Cache DOM elements
     */
    cacheElements() {
        this.elements = {
            screenerBtns: document.querySelectorAll('.screener-btn'),
            filtersContainer: document.getElementById('filters-container'),
            noFilters: document.getElementById('no-filters'),
            addFilterBtn: document.getElementById('add-filter-btn'),
            fieldSearch: document.getElementById('field-search'),
            fieldCategory: document.getElementById('field-category'),
            fieldsContainer: document.getElementById('fields-container'),
            fieldCounter: document.getElementById('field-counter'),
            selectAllBtn: document.getElementById('select-all-btn'),
            clearAllBtn: document.getElementById('clear-all-btn'),
            presetsBtn: document.getElementById('presets-btn'),
            presetsMenu: document.getElementById('presets-menu'),
            indexGroup: document.getElementById('index-group'),
            indexSelect: document.getElementById('index-select'),
            sortField: document.getElementById('sort-field'),
            sortOrder: document.getElementById('sort-order'),
            limitInput: document.getElementById('limit-input'),
            optionsToggle: document.getElementById('options-toggle'),
            optionsSection: document.getElementById('options-section'),
            generatedCode: document.getElementById('generated-code'),
            copyBtn: document.getElementById('copy-btn'),
            filterTemplate: document.getElementById('filter-template')
        };
    },

    /**
     * Populate index dropdown
     */
    populateIndices() {
        for (const idx of FIELD_DATA.indices) {
            const option = document.createElement('option');
            option.value = idx.name;
            option.textContent = idx.label;
            this.elements.indexSelect.appendChild(option);
        }
    },

    /**
     * Populate categories dropdown
     */
    populateCategories() {
        this.elements.fieldCategory.innerHTML = '<option value="">All Categories</option>';
        const fields = this.getFields();
        const categories = [...new Set(fields.map(f => f.category))].sort();
        for (const cat of categories) {
            const option = document.createElement('option');
            option.value = cat;
            option.textContent = cat;
            this.elements.fieldCategory.appendChild(option);
        }
    },

    /**
     * Populate sort field dropdown
     */
    populateSortFields() {
        this.elements.sortField.innerHTML = '<option value="">Default</option>';
        const fields = this.getFields();
        const commonSortFields = [
            'MARKET_CAPITALIZATION', 'PRICE', 'CHANGE_PERCENT', 'VOLUME',
            'PE_RATIO_TTM', 'DIVIDEND_YIELD_FY', 'RELATIVE_STRENGTH_INDEX_14'
        ];
        for (const fieldName of commonSortFields) {
            const field = fields.find(f => f.name === fieldName);
            if (field) {
                const option = document.createElement('option');
                option.value = field.name;
                option.textContent = field.label;
                this.elements.sortField.appendChild(option);
            }
        }
    },

    /**
     * Render field checkboxes
     */
    renderFields() {
        const container = this.elements.fieldsContainer;
        container.innerHTML = '';

        const allFields = this.getFields();
        const searchTerm = this.elements.fieldSearch.value.toLowerCase();
        const category = this.elements.fieldCategory.value;

        // Common fields to show first
        const commonFields = ['NAME', 'PRICE', 'CHANGE_PERCENT', 'VOLUME', 'MARKET_CAPITALIZATION',
            'PE_RATIO_TTM', 'DIVIDEND_YIELD_FY', 'RELATIVE_STRENGTH_INDEX_14', 'MACD_LEVEL_12_26',
            'SIMPLE_MOVING_AVERAGE_50', 'SIMPLE_MOVING_AVERAGE_200', 'PERFORMANCE_1_WEEK',
            'PERFORMANCE_1_MONTH', 'SECTOR', 'INDUSTRY', 'BID', 'ASK', 'YIELD'];

        let fields = allFields.filter(f => {
            if (searchTerm && !f.label.toLowerCase().includes(searchTerm) && !f.name.toLowerCase().includes(searchTerm)) {
                return false;
            }
            if (category && f.category !== category) {
                return false;
            }
            return true;
        });

        // Sort: common fields first, then alphabetically
        fields.sort((a, b) => {
            const aCommon = commonFields.includes(a.name);
            const bCommon = commonFields.includes(b.name);
            if (aCommon && !bCommon) return -1;
            if (!aCommon && bCommon) return 1;
            return a.label.localeCompare(b.label);
        });

        // Limit display to prevent lag
        const displayFields = fields.slice(0, 150);

        for (const field of displayFields) {
            const item = document.createElement('div');
            item.className = 'field-item';

            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = `field-${field.name}`;
            checkbox.value = field.name;
            checkbox.checked = this.state.selectAll || this.state.selectedFields.includes(field.name);
            checkbox.addEventListener('change', () => this.toggleField(field.name, checkbox.checked));

            const label = document.createElement('label');
            label.htmlFor = `field-${field.name}`;
            label.textContent = field.label;
            label.title = `${field.name} (${field.category})`;

            item.appendChild(checkbox);
            item.appendChild(label);
            container.appendChild(item);
        }

        if (fields.length > 150) {
            const note = document.createElement('div');
            note.className = 'fields-empty';
            note.textContent = `Showing 150 of ${fields.length} fields. Use search to find more.`;
            container.appendChild(note);
        }

        if (fields.length === 0) {
            const note = document.createElement('div');
            note.className = 'fields-empty';
            note.textContent = 'No fields match your search.';
            container.appendChild(note);
        }
    },

    /**
     * Update field counter
     */
    updateFieldCounter() {
        const count = this.state.selectAll
            ? this.getFields().length
            : this.state.selectedFields.length;

        if (this.state.selectAll) {
            this.elements.fieldCounter.textContent = `All ${count} fields`;
        } else if (count === 0) {
            this.elements.fieldCounter.textContent = 'Default fields';
        } else {
            this.elements.fieldCounter.textContent = `${count} selected`;
        }
    },

    /**
     * Bind event listeners
     */
    bindEvents() {
        // Screener buttons
        this.elements.screenerBtns.forEach(btn => {
            btn.addEventListener('click', () => this.switchScreener(btn.dataset.screener));
        });

        // Add filter button
        this.elements.addFilterBtn.addEventListener('click', () => this.addFilter());

        // Field search
        this.elements.fieldSearch.addEventListener('input', () => this.renderFields());

        // Field category filter
        this.elements.fieldCategory.addEventListener('change', () => this.renderFields());

        // Select all button
        this.elements.selectAllBtn.addEventListener('click', () => this.selectAllFields());

        // Clear all button
        this.elements.clearAllBtn.addEventListener('click', () => this.clearAllFields());

        // Presets dropdown
        this.elements.presetsBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            this.elements.presetsBtn.parentElement.classList.toggle('open');
        });

        document.addEventListener('click', () => {
            this.elements.presetsBtn.parentElement.classList.remove('open');
        });

        // Preset items
        this.elements.presetsMenu.querySelectorAll('.dropdown-item').forEach(item => {
            item.addEventListener('click', () => {
                this.applyPreset(item.dataset.preset);
                this.elements.presetsBtn.parentElement.classList.remove('open');
            });
        });

        // Options toggle
        this.elements.optionsToggle.addEventListener('click', () => {
            this.elements.optionsSection.classList.toggle('collapsed');
            this.elements.optionsToggle.classList.toggle('collapsed');
        });

        // Index select
        this.elements.indexSelect.addEventListener('change', (e) => {
            this.state.index = e.target.value;
            this.updateCode();
        });

        // Sort field
        this.elements.sortField.addEventListener('change', (e) => {
            this.state.sortField = e.target.value;
            this.updateCode();
        });

        // Sort order
        this.elements.sortOrder.addEventListener('change', (e) => {
            this.state.sortOrder = e.target.value;
            this.updateCode();
        });

        // Limit input
        this.elements.limitInput.addEventListener('input', (e) => {
            this.state.limit = parseInt(e.target.value) || 100;
            this.updateCode();
        });

        // Copy button
        this.elements.copyBtn.addEventListener('click', () => this.copyCode());
    },

    /**
     * Switch screener type
     */
    switchScreener(type) {
        this.state.screenerType = type;
        this.state.selectedFields = [];
        this.state.selectAll = false;
        this.state.filters = [];
        this.state.index = '';
        this.state.sortField = '';

        // Update active button
        this.elements.screenerBtns.forEach(btn => {
            btn.classList.toggle('active', btn.dataset.screener === type);
        });

        // Show/hide index filter (only for stocks)
        const config = this.getScreenerConfig();
        this.elements.indexGroup.classList.toggle('hidden', !config.hasIndex);

        // Rebuild UI for new screener
        this.elements.filtersContainer.innerHTML = '';
        this.populateCategories();
        this.populateSortFields();
        this.renderFields();
        this.updateFieldCounter();
        this.updateCode();
        this.updateNoFiltersHint();
    },

    /**
     * Add a new filter row
     */
    addFilter() {
        const template = this.elements.filterTemplate.content.cloneNode(true);
        const row = template.querySelector('.filter-row');
        const filterId = Date.now();
        row.dataset.filterId = filterId;

        // Populate field select
        const fieldSelect = row.querySelector('.filter-field');
        const fields = this.getFields();
        const commonFields = ['PRICE', 'VOLUME', 'MARKET_CAPITALIZATION', 'CHANGE_PERCENT',
            'PE_RATIO_TTM', 'DIVIDEND_YIELD_FY', 'RELATIVE_STRENGTH_INDEX_14'];

        // Add common fields first
        const optgroup1 = document.createElement('optgroup');
        optgroup1.label = 'Common';
        for (const fieldName of commonFields) {
            const field = fields.find(f => f.name === fieldName);
            if (field) {
                const option = document.createElement('option');
                option.value = field.name;
                option.textContent = field.label;
                option.dataset.format = field.format;
                optgroup1.appendChild(option);
            }
        }
        if (optgroup1.children.length > 0) {
            fieldSelect.appendChild(optgroup1);
        }

        // Group remaining by category
        const categories = [...new Set(fields.map(f => f.category))].sort();
        for (const cat of categories) {
            const catFields = fields.filter(f => f.category === cat && !commonFields.includes(f.name));
            if (catFields.length > 0) {
                const optgroup = document.createElement('optgroup');
                optgroup.label = cat;
                for (const field of catFields.slice(0, 25)) {
                    const option = document.createElement('option');
                    option.value = field.name;
                    option.textContent = field.label;
                    option.dataset.format = field.format;
                    optgroup.appendChild(option);
                }
                fieldSelect.appendChild(optgroup);
            }
        }

        // Bind events
        const operatorSelect = row.querySelector('.filter-operator');
        const valueInput = row.querySelector('.filter-value');
        const value2Input = row.querySelector('.filter-value2');
        const removeBtn = row.querySelector('.btn-remove');

        fieldSelect.addEventListener('change', () => this.updateFilterState(filterId));
        operatorSelect.addEventListener('change', () => {
            value2Input.style.display = operatorSelect.value === 'between' ? 'block' : 'none';
            this.updateFilterState(filterId);
        });
        valueInput.addEventListener('input', () => this.updateFilterState(filterId));
        value2Input.addEventListener('input', () => this.updateFilterState(filterId));

        removeBtn.addEventListener('click', () => {
            row.remove();
            this.state.filters = this.state.filters.filter(f => f.id !== filterId);
            this.updateCode();
            this.updateNoFiltersHint();
        });

        // Add to DOM
        this.elements.filtersContainer.appendChild(row);

        // Initialize filter state
        this.state.filters.push({
            id: filterId,
            field: '',
            operator: '>',
            value: '',
            value2: '',
            format: ''
        });

        this.updateNoFiltersHint();
    },

    /**
     * Update no filters hint visibility
     */
    updateNoFiltersHint() {
        const hasFilters = this.elements.filtersContainer.children.length > 0;
        this.elements.noFilters.style.display = hasFilters ? 'none' : 'block';
    },

    /**
     * Update filter state from DOM
     */
    updateFilterState(filterId) {
        const row = document.querySelector(`[data-filter-id="${filterId}"]`);
        if (!row) return;

        const fieldSelect = row.querySelector('.filter-field');
        const operatorSelect = row.querySelector('.filter-operator');
        const valueInput = row.querySelector('.filter-value');
        const value2Input = row.querySelector('.filter-value2');

        const selectedOption = fieldSelect.options[fieldSelect.selectedIndex];
        const format = selectedOption?.dataset?.format || '';

        const filter = this.state.filters.find(f => f.id === filterId);
        if (filter) {
            filter.field = fieldSelect.value;
            filter.operator = operatorSelect.value;
            filter.value = valueInput.value;
            filter.value2 = value2Input.value;
            filter.format = format;
        }

        this.updateCode();
    },

    /**
     * Toggle field selection
     */
    toggleField(fieldName, checked) {
        if (this.state.selectAll) {
            // If select all is on, switching to manual selection
            this.state.selectAll = false;
            this.state.selectedFields = this.getFields().map(f => f.name);
        }

        if (checked) {
            if (!this.state.selectedFields.includes(fieldName)) {
                this.state.selectedFields.push(fieldName);
            }
        } else {
            this.state.selectedFields = this.state.selectedFields.filter(f => f !== fieldName);
        }

        this.updateFieldCounter();
        this.updateCode();
    },

    /**
     * Select all fields
     */
    selectAllFields() {
        this.state.selectAll = true;
        this.state.selectedFields = [];
        this.renderFields();
        this.updateFieldCounter();
        this.updateCode();
    },

    /**
     * Clear all selected fields
     */
    clearAllFields() {
        this.state.selectAll = false;
        this.state.selectedFields = [];
        this.renderFields();
        this.updateFieldCounter();
        this.updateCode();
    },

    /**
     * Apply a preset
     */
    applyPreset(presetName) {
        this.state.selectAll = false;
        const screenerPresets = this.presets[this.state.screenerType] || this.presets.stock;
        const preset = screenerPresets[presetName];
        if (preset) {
            this.state.selectedFields = [...preset];
        }
        this.renderFields();
        this.updateFieldCounter();
        this.updateCode();
    },

    /**
     * Update generated code
     */
    updateCode() {
        const config = {
            screenerType: this.state.screenerType,
            screenerConfig: this.getScreenerConfig(),
            filters: this.state.filters.filter(f => f.field && f.value),
            fields: this.state.selectedFields,
            selectAll: this.state.selectAll,
            index: this.state.index,
            sortField: this.state.sortField,
            sortOrder: this.state.sortOrder,
            limit: this.state.limit
        };

        const code = CodeGenerator.generate(config);
        this.elements.generatedCode.textContent = code;
        hljs.highlightElement(this.elements.generatedCode);
    },

    /**
     * Copy code to clipboard
     */
    async copyCode() {
        const code = this.elements.generatedCode.textContent;
        try {
            await navigator.clipboard.writeText(code);
            this.elements.copyBtn.classList.add('copied');
            this.elements.copyBtn.querySelector('span').textContent = 'Copied!';
            setTimeout(() => {
                this.elements.copyBtn.classList.remove('copied');
                this.elements.copyBtn.querySelector('span').textContent = 'Copy';
            }, 2000);
        } catch (err) {
            console.error('Failed to copy:', err);
        }
    }
};

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => App.init());
