/**
 * tvscreener Code Generator - Main Application
 */

const App = {
    // State
    state: {
        screenerType: 'stock',
        filters: [],
        selectedFields: [],
        index: '',
        sortField: '',
        sortOrder: 'desc',
        limit: 100
    },

    // DOM Elements
    elements: {},

    // Field presets
    presets: {
        basic: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'VOLUME', 'MARKET_CAPITALIZATION'],
        valuation: ['NAME', 'PRICE', 'PE_RATIO_TTM', 'PRICE_TO_BOOK_FY', 'PRICE_TO_SALES_FY', 'EV_TO_EBITDA_TTM', 'MARKET_CAPITALIZATION'],
        technical: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'RELATIVE_STRENGTH_INDEX_14', 'MACD_LEVEL_12_26', 'SIMPLE_MOVING_AVERAGE_50', 'SIMPLE_MOVING_AVERAGE_200'],
        performance: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'PERFORMANCE_1_WEEK', 'PERFORMANCE_1_MONTH', 'PERFORMANCE_3_MONTH', 'PERFORMANCE_YEAR_TO_DATE']
    },

    /**
     * Initialize the application
     */
    init() {
        this.cacheElements();
        this.populateSelects();
        this.renderFields();
        this.bindEvents();
        this.addFilter(); // Add one empty filter by default
        this.updateCode();
    },

    /**
     * Cache DOM elements
     */
    cacheElements() {
        this.elements = {
            screenerType: document.getElementById('screener-type'),
            filtersContainer: document.getElementById('filters-container'),
            addFilterBtn: document.getElementById('add-filter-btn'),
            fieldSearch: document.getElementById('field-search'),
            fieldCategory: document.getElementById('field-category'),
            fieldsContainer: document.getElementById('fields-container'),
            indexSelect: document.getElementById('index-select'),
            sortField: document.getElementById('sort-field'),
            sortOrder: document.getElementById('sort-order'),
            limitInput: document.getElementById('limit-input'),
            generatedCode: document.getElementById('generated-code'),
            copyBtn: document.getElementById('copy-btn'),
            filterTemplate: document.getElementById('filter-template')
        };
    },

    /**
     * Populate select dropdowns with data
     */
    populateSelects() {
        // Populate category filter
        const categories = [...new Set(FIELD_DATA.fields.map(f => f.category))].sort();
        for (const cat of categories) {
            const option = document.createElement('option');
            option.value = cat;
            option.textContent = cat;
            this.elements.fieldCategory.appendChild(option);
        }

        // Populate index select
        for (const idx of FIELD_DATA.indices) {
            const option = document.createElement('option');
            option.value = idx.name;
            option.textContent = idx.label;
            this.elements.indexSelect.appendChild(option);
        }

        // Populate sort field select
        const commonSortFields = [
            'MARKET_CAPITALIZATION', 'PRICE', 'CHANGE_PERCENT', 'VOLUME',
            'PE_RATIO_TTM', 'DIVIDEND_YIELD_FY', 'RELATIVE_STRENGTH_INDEX_14'
        ];
        for (const fieldName of commonSortFields) {
            const field = FIELD_DATA.fields.find(f => f.name === fieldName);
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

        // Get filtered fields
        const searchTerm = this.elements.fieldSearch.value.toLowerCase();
        const category = this.elements.fieldCategory.value;

        // Group common fields first
        const commonFields = ['NAME', 'PRICE', 'CHANGE_PERCENT', 'VOLUME', 'MARKET_CAPITALIZATION',
            'PE_RATIO_TTM', 'DIVIDEND_YIELD_FY', 'RELATIVE_STRENGTH_INDEX_14', 'MACD_LEVEL_12_26',
            'SIMPLE_MOVING_AVERAGE_50', 'SIMPLE_MOVING_AVERAGE_200', 'PERFORMANCE_1_WEEK',
            'PERFORMANCE_1_MONTH', 'SECTOR', 'INDUSTRY'];

        let fields = FIELD_DATA.fields.filter(f => {
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
        const displayFields = fields.slice(0, 200);

        for (const field of displayFields) {
            const item = document.createElement('div');
            item.className = 'field-item';

            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = `field-${field.name}`;
            checkbox.value = field.name;
            checkbox.checked = this.state.selectedFields.includes(field.name);
            checkbox.addEventListener('change', () => this.toggleField(field.name));

            const label = document.createElement('label');
            label.htmlFor = `field-${field.name}`;
            label.textContent = field.label;
            label.title = `${field.name} (${field.category})`;

            item.appendChild(checkbox);
            item.appendChild(label);
            container.appendChild(item);
        }

        if (fields.length > 200) {
            const note = document.createElement('div');
            note.className = 'empty-state';
            note.textContent = `Showing 200 of ${fields.length} fields. Use search to find more.`;
            container.appendChild(note);
        }

        if (fields.length === 0) {
            const note = document.createElement('div');
            note.className = 'empty-state';
            note.textContent = 'No fields match your search.';
            container.appendChild(note);
        }
    },

    /**
     * Bind event listeners
     */
    bindEvents() {
        // Screener type change
        this.elements.screenerType.addEventListener('change', (e) => {
            this.state.screenerType = e.target.value;
            this.updateCode();
        });

        // Add filter button
        this.elements.addFilterBtn.addEventListener('click', () => this.addFilter());

        // Field search
        this.elements.fieldSearch.addEventListener('input', () => this.renderFields());

        // Field category filter
        this.elements.fieldCategory.addEventListener('change', () => this.renderFields());

        // Preset buttons
        document.querySelectorAll('.preset-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const preset = e.target.dataset.preset;
                this.applyPreset(preset);
            });
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
     * Add a new filter row
     */
    addFilter() {
        const template = this.elements.filterTemplate.content.cloneNode(true);
        const row = template.querySelector('.filter-row');
        const filterId = Date.now();
        row.dataset.filterId = filterId;

        // Populate field select
        const fieldSelect = row.querySelector('.filter-field');
        const commonFields = ['PRICE', 'VOLUME', 'MARKET_CAPITALIZATION', 'CHANGE_PERCENT',
            'PE_RATIO_TTM', 'DIVIDEND_YIELD_FY', 'RELATIVE_STRENGTH_INDEX_14'];

        // Add common fields first
        const optgroup1 = document.createElement('optgroup');
        optgroup1.label = 'Common';
        for (const fieldName of commonFields) {
            const field = FIELD_DATA.fields.find(f => f.name === fieldName);
            if (field) {
                const option = document.createElement('option');
                option.value = field.name;
                option.textContent = field.label;
                option.dataset.format = field.format;
                optgroup1.appendChild(option);
            }
        }
        fieldSelect.appendChild(optgroup1);

        // Group remaining by category
        const categories = [...new Set(FIELD_DATA.fields.map(f => f.category))].sort();
        for (const cat of categories) {
            const catFields = FIELD_DATA.fields.filter(f => f.category === cat && !commonFields.includes(f.name));
            if (catFields.length > 0) {
                const optgroup = document.createElement('optgroup');
                optgroup.label = cat;
                for (const field of catFields.slice(0, 30)) { // Limit per category
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
        const removeBtn = row.querySelector('.remove-filter');

        fieldSelect.addEventListener('change', () => {
            this.updateFilterState(filterId);
        });

        operatorSelect.addEventListener('change', () => {
            // Show/hide second value input for 'between'
            value2Input.style.display = operatorSelect.value === 'between' ? 'block' : 'none';
            this.updateFilterState(filterId);
        });

        valueInput.addEventListener('input', () => this.updateFilterState(filterId));
        value2Input.addEventListener('input', () => this.updateFilterState(filterId));

        removeBtn.addEventListener('click', () => {
            row.remove();
            this.state.filters = this.state.filters.filter(f => f.id !== filterId);
            this.updateCode();
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
    toggleField(fieldName) {
        const idx = this.state.selectedFields.indexOf(fieldName);
        if (idx === -1) {
            this.state.selectedFields.push(fieldName);
        } else {
            this.state.selectedFields.splice(idx, 1);
        }
        this.updateCode();
    },

    /**
     * Apply a preset
     */
    applyPreset(presetName) {
        if (presetName === 'clear') {
            this.state.selectedFields = [];
        } else if (this.presets[presetName]) {
            this.state.selectedFields = [...this.presets[presetName]];
        }
        this.renderFields();
        this.updateCode();
    },

    /**
     * Update generated code
     */
    updateCode() {
        const config = {
            screenerType: this.state.screenerType,
            filters: this.state.filters.filter(f => f.field && f.value),
            fields: this.state.selectedFields,
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
            this.elements.copyBtn.classList.add('btn-copied');
            this.elements.copyBtn.innerHTML = `
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
                Copied!
            `;
            setTimeout(() => {
                this.elements.copyBtn.classList.remove('btn-copied');
                this.elements.copyBtn.innerHTML = `
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                    </svg>
                    Copy
                `;
            }, 2000);
        } catch (err) {
            console.error('Failed to copy:', err);
        }
    }
};

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => App.init());
