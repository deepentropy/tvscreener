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
        sortInterval: '',
        sortOrder: 'desc',
        fieldsInterval: '',
        markets: [],
        limit: 100
    },

    // DOM Elements
    elements: {},

    // Code lines of the last render, used to flag changed lines
    previousLines: null,

    // Screener tab labels
    screenerLabels: {
        stock: 'Stock',
        crypto: 'Crypto',
        forex: 'Forex',
        bond: 'Bond',
        futures: 'Futures',
        coin: 'Coin'
    },

    // Preset labels
    presetLabels: {
        basic: 'Basic',
        valuation: 'Valuation',
        technical: 'Technical',
        performance: 'Performance',
        dividends: 'Dividends'
    },

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

    // Fields listed first in the field list and the filter picker
    commonFields: ['NAME', 'PRICE', 'CHANGE_PERCENT', 'VOLUME', 'MARKET_CAPITALIZATION',
        'PE_RATIO_TTM', 'DIVIDEND_YIELD_FY', 'RELATIVE_STRENGTH_INDEX_14', 'MACD_LEVEL_12_26',
        'SIMPLE_MOVING_AVERAGE_50', 'SIMPLE_MOVING_AVERAGE_200', 'PERFORMANCE_1_WEEK',
        'PERFORMANCE_1_MONTH', 'SECTOR', 'INDUSTRY', 'BID', 'ASK', 'YIELD'],

    commonFilterFields: ['PRICE', 'VOLUME', 'MARKET_CAPITALIZATION', 'CHANGE_PERCENT',
        'PE_RATIO_TTM', 'DIVIDEND_YIELD_FY', 'RELATIVE_STRENGTH_INDEX_14'],

    commonSortFields: ['MARKET_CAPITALIZATION', 'PRICE', 'CHANGE_PERCENT', 'VOLUME',
        'PE_RATIO_TTM', 'DIVIDEND_YIELD_FY', 'RELATIVE_STRENGTH_INDEX_14'],

    // Timeframes for with_interval(); '' is the daily default and adds no suffix
    timeframes: [
        { value: '1', label: '1m' },
        { value: '5', label: '5m' },
        { value: '15', label: '15m' },
        { value: '30', label: '30m' },
        { value: '60', label: '1h' },
        { value: '120', label: '2h' },
        { value: '240', label: '4h' },
        { value: '', label: '1D' },
        { value: '1W', label: '1W' },
        { value: '1M', label: '1M' }
    ],

    // Maximum rows rendered in the field list
    MAX_FIELD_ROWS: 300,

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

    findField(name) {
        return this.getFields().find(f => f.name === name);
    },

    /**
     * Fill a select with the timeframes, daily selected
     */
    populateTimeframes(select) {
        for (const tf of this.timeframes) {
            const option = document.createElement('option');
            option.value = tf.value;
            option.textContent = tf.label;
            option.selected = tf.value === '';
            select.appendChild(option);
        }
    },

    marketLabel(name) {
        return FIELD_DATA.markets.find(m => m.name === name)?.label || name;
    },

    /**
     * Render the market chips and the "add market" select
     */
    renderMarkets() {
        const { marketSelect, marketChips } = this.elements;
        const markets = this.state.markets;

        marketSelect.innerHTML = '';
        const first = document.createElement('option');
        first.value = '';
        first.textContent = markets.length
            ? 'Add market'
            : `${this.marketLabel(FIELD_DATA.defaultMarket)} (default)`;
        marketSelect.appendChild(first);
        for (const m of FIELD_DATA.markets) {
            if (markets.includes(m.name)) continue;
            const option = document.createElement('option');
            option.value = m.name;
            option.textContent = m.label;
            marketSelect.appendChild(option);
        }
        marketSelect.value = '';

        marketChips.innerHTML = '';
        for (const name of markets) {
            const chip = document.createElement('button');
            chip.type = 'button';
            chip.className = 'chip';
            chip.title = `Remove ${this.marketLabel(name)}`;
            chip.innerHTML = '<span class="chip-text"></span><span class="chip-x" aria-hidden="true">×</span>';
            chip.querySelector('.chip-text').textContent = this.marketLabel(name);
            chip.addEventListener('click', () => {
                this.state.markets = this.state.markets.filter(n => n !== name);
                this.renderMarkets();
                this.updateCode();
            });
            marketChips.appendChild(chip);
        }
    },

    /**
     * Show the columns timeframe when indicator columns are selected
     */
    updateFieldsInterval() {
        const total = this.state.selectedFields.length;
        const count = this.state.selectedFields.filter(n => this.findField(n)?.interval).length;
        this.elements.fieldsIntervalGroup.hidden = this.state.selectAll || count === 0;
        this.elements.fieldsIntervalHint.textContent = `Applies to ${count} of ${total} columns`;
    },

    /**
     * Show a timeframe select only when the field supports it; reset it otherwise
     * @returns {boolean} true when the field supports a timeframe
     */
    syncIntervalSelect(select, field) {
        const supported = !!field?.interval;
        select.hidden = !supported;
        if (!supported) select.value = '';
        return supported;
    },

    /**
     * Initialize the application
     */
    init() {
        this.cacheElements();
        this.renderScreenerTabs();
        this.populateIndices();
        this.populateTimeframes(this.elements.fieldsInterval);
        this.populateTimeframes(this.elements.sortInterval);
        this.createSortPicker();
        this.bindEvents();
        this.refreshScreenerUI();
    },

    /**
     * Cache DOM elements
     */
    cacheElements() {
        this.elements = {
            screenerTabs: document.getElementById('screener-tabs'),
            fieldsIntervalGroup: document.getElementById('fields-interval-group'),
            fieldsInterval: document.getElementById('fields-interval'),
            fieldsIntervalHint: document.getElementById('fields-interval-hint'),
            sortInterval: document.getElementById('sort-interval'),
            marketGroup: document.getElementById('market-group'),
            marketSelect: document.getElementById('market-select'),
            marketChips: document.getElementById('market-chips'),
            filtersContainer: document.getElementById('filters-container'),
            noFilters: document.getElementById('no-filters'),
            addFilterBtn: document.getElementById('add-filter-btn'),
            fieldSearch: document.getElementById('field-search'),
            fieldCategory: document.getElementById('field-category'),
            fieldsContainer: document.getElementById('fields-container'),
            fieldCounter: document.getElementById('field-counter'),
            selectedChips: document.getElementById('selected-chips'),
            selectAllBtn: document.getElementById('select-all-btn'),
            clearAllBtn: document.getElementById('clear-all-btn'),
            presets: document.getElementById('presets'),
            indexGroup: document.getElementById('index-group'),
            indexSelect: document.getElementById('index-select'),
            sortSlot: document.getElementById('sort-field-slot'),
            sortOrderBtns: document.querySelectorAll('.toggle-btn[data-order]'),
            limitInput: document.getElementById('limit-input'),
            generatedCode: document.getElementById('generated-code'),
            copyBtn: document.getElementById('copy-btn'),
            filterTemplate: document.getElementById('filter-template')
        };
    },

    /**
     * Render the screener tabs with their field counts
     */
    renderScreenerTabs() {
        const nav = this.elements.screenerTabs;
        nav.dataset.section = 'screener';
        for (const [key, config] of Object.entries(FIELD_DATA.screeners)) {
            const btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'screener-tab';
            btn.dataset.screener = key;
            btn.setAttribute('role', 'tab');
            btn.title = `${config.name}: ${config.fields.length.toLocaleString('en-US')} fields`;

            const label = document.createElement('span');
            label.className = 'tab-label';
            label.textContent = this.screenerLabels[key] || config.name;

            const count = document.createElement('span');
            count.className = 'tab-count';
            count.textContent = config.fields.length.toLocaleString('en-US');

            btn.append(label, count);
            btn.addEventListener('click', () => this.switchScreener(key));
            nav.appendChild(btn);
        }
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
        this.elements.fieldCategory.innerHTML = '<option value="">All categories</option>';
        const categories = [...new Set(this.getFields().map(f => f.category))].sort();
        for (const cat of categories) {
            const option = document.createElement('option');
            option.value = cat;
            option.textContent = cat;
            this.elements.fieldCategory.appendChild(option);
        }
    },

    /**
     * Render preset buttons available for the current screener
     */
    renderPresets() {
        const container = this.elements.presets;
        container.innerHTML = '';
        const screenerPresets = this.presets[this.state.screenerType] || {};
        for (const name of Object.keys(screenerPresets)) {
            const btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'preset';
            btn.textContent = this.presetLabels[name] || name;
            btn.addEventListener('click', () => this.applyPreset(name));
            container.appendChild(btn);
        }
    },

    /**
     * Create the searchable sort field picker
     */
    createSortPicker() {
        this.sortPicker = FieldPicker.create({
            getFields: () => this.getFields(),
            pinned: this.commonSortFields,
            placeholder: 'Default order',
            clearable: true,
            onChange: (field) => {
                this.state.sortField = field ? field.name : '';
                if (!this.syncIntervalSelect(this.elements.sortInterval, field)) this.state.sortInterval = '';
                this.updateCode();
            }
        });
        this.elements.sortSlot.appendChild(this.sortPicker.el);
    },

    /**
     * Render field rows
     */
    renderFields() {
        const container = this.elements.fieldsContainer;
        container.innerHTML = '';

        const category = this.elements.fieldCategory.value;
        const inCategory = this.getFields().filter(f => !category || f.category === category);
        const fields = FieldSearch.search(inCategory, this.elements.fieldSearch.value, this.commonFields);

        const fragment = document.createDocumentFragment();
        for (const field of fields.slice(0, this.MAX_FIELD_ROWS)) {
            const row = document.createElement('label');
            row.className = 'field-row';
            row.title = `${field.name} (${field.category})`;

            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.className = 'check';
            checkbox.value = field.name;
            checkbox.checked = this.state.selectAll || this.state.selectedFields.includes(field.name);
            checkbox.addEventListener('change', () => this.toggleField(field.name, checkbox.checked));

            const label = document.createElement('span');
            label.className = 'field-label';
            label.textContent = field.label;

            const name = document.createElement('span');
            name.className = 'field-name';
            name.textContent = field.name;

            row.append(checkbox, label, name);
            fragment.appendChild(row);
        }
        container.appendChild(fragment);

        if (fields.length > this.MAX_FIELD_ROWS) {
            this.appendListNote(`${this.MAX_FIELD_ROWS} of ${fields.length.toLocaleString('en-US')} fields shown. Search to find the others.`);
        } else if (fields.length === 0) {
            this.appendListNote('No field matches this search.');
        }
    },

    appendListNote(text) {
        const note = document.createElement('p');
        note.className = 'field-list-note';
        note.textContent = text;
        this.elements.fieldsContainer.appendChild(note);
    },

    /**
     * Sync checkboxes with the state without rebuilding the list
     */
    syncCheckboxes() {
        this.elements.fieldsContainer.querySelectorAll('.check').forEach(cb => {
            cb.checked = this.state.selectAll || this.state.selectedFields.includes(cb.value);
        });
    },

    /**
     * Render the chips of selected fields, in select() order
     */
    renderChips() {
        const container = this.elements.selectedChips;
        container.innerHTML = '';

        if (this.state.selectAll) {
            const chip = document.createElement('span');
            chip.className = 'chip chip-all';
            chip.textContent = `All ${this.getFields().length.toLocaleString('en-US')} fields`;
            container.appendChild(chip);
            return;
        }

        for (const name of this.state.selectedFields) {
            const field = this.findField(name);
            const chip = document.createElement('button');
            chip.type = 'button';
            chip.className = 'chip';
            chip.title = `Remove ${field ? field.label : name}`;
            chip.innerHTML = '<span class="chip-text"></span><span class="chip-x" aria-hidden="true">×</span>';
            chip.querySelector('.chip-text').textContent = field ? field.label : name;
            chip.addEventListener('click', () => this.toggleField(name, false));
            container.appendChild(chip);
        }
    },

    /**
     * Update field counter
     */
    updateFieldCounter() {
        const counter = this.elements.fieldCounter;
        if (this.state.selectAll) {
            counter.textContent = `All ${this.getFields().length.toLocaleString('en-US')}`;
        } else if (this.state.selectedFields.length === 0) {
            counter.textContent = 'Default';
        } else {
            counter.textContent = `${this.state.selectedFields.length} selected`;
        }
        counter.classList.toggle('count-active', this.state.selectAll || this.state.selectedFields.length > 0);
    },

    /**
     * Bind event listeners
     */
    bindEvents() {
        this.elements.addFilterBtn.addEventListener('click', () => this.addFilter());
        this.elements.fieldSearch.addEventListener('input', () => this.renderFields());
        this.elements.fieldCategory.addEventListener('change', () => this.renderFields());
        this.elements.selectAllBtn.addEventListener('click', () => this.selectAllFields());
        this.elements.clearAllBtn.addEventListener('click', () => this.clearAllFields());

        this.elements.indexSelect.addEventListener('change', (e) => {
            this.state.index = e.target.value;
            this.updateCode();
        });

        this.elements.marketSelect.addEventListener('change', (e) => {
            const name = e.target.value;
            if (!name) return;
            // "All markets" replaces the other markets, and the other way round
            this.state.markets = name === 'ALL'
                ? ['ALL']
                : [...this.state.markets.filter(n => n !== 'ALL'), name];
            this.renderMarkets();
            this.updateCode();
        });

        this.elements.fieldsInterval.addEventListener('change', (e) => {
            this.state.fieldsInterval = e.target.value;
            this.updateCode();
        });

        this.elements.sortInterval.addEventListener('change', (e) => {
            this.state.sortInterval = e.target.value;
            this.updateCode();
        });

        this.elements.sortOrderBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                this.state.sortOrder = btn.dataset.order;
                this.elements.sortOrderBtns.forEach(b => {
                    const on = b === btn;
                    b.classList.toggle('active', on);
                    b.setAttribute('aria-pressed', String(on));
                });
                this.updateCode();
            });
        });

        this.elements.limitInput.addEventListener('input', (e) => {
            this.state.limit = parseInt(e.target.value) || 100;
            this.updateCode();
        });

        this.elements.copyBtn.addEventListener('click', () => this.copyCode());

        // Highlight the code lines produced by the hovered or focused section
        const code = this.elements.generatedCode;
        document.querySelectorAll('[data-section]').forEach(section => {
            if (section.classList.contains('line')) return;
            const on = () => {
                // Only dim the code when the section produced lines
                const name = section.dataset.section;
                if (code.querySelector(`.line[data-section="${name}"]`)) code.dataset.focus = name;
                else delete code.dataset.focus;
            };
            const off = () => { delete code.dataset.focus; };
            section.addEventListener('mouseenter', on);
            section.addEventListener('mouseleave', off);
            section.addEventListener('focusin', on);
            section.addEventListener('focusout', off);
        });
    },

    /**
     * Switch screener type
     */
    switchScreener(type) {
        if (type === this.state.screenerType) return;
        this.state.screenerType = type;
        this.state.selectedFields = [];
        this.state.selectAll = false;
        this.state.filters = [];
        this.state.index = '';
        this.state.sortField = '';
        this.state.sortInterval = '';
        this.state.fieldsInterval = '';
        this.state.markets = [];

        this.elements.filtersContainer.innerHTML = '';
        this.elements.indexSelect.value = '';
        this.elements.fieldSearch.value = '';
        this.elements.fieldsInterval.value = '';
        this.sortPicker.setValue(null);
        this.syncIntervalSelect(this.elements.sortInterval, null);
        FieldPicker.close();

        this.refreshScreenerUI();
    },

    /**
     * Rebuild the parts of the UI that depend on the screener
     */
    refreshScreenerUI() {
        this.elements.screenerTabs.querySelectorAll('.screener-tab').forEach(btn => {
            const on = btn.dataset.screener === this.state.screenerType;
            btn.classList.toggle('active', on);
            btn.setAttribute('aria-selected', String(on));
        });

        // Index and markets only exist for stocks
        const config = this.getScreenerConfig();
        this.elements.indexGroup.hidden = !config.hasIndex;
        this.elements.marketGroup.hidden = !config.hasMarket;
        this.renderMarkets();

        this.populateCategories();
        this.renderPresets();
        this.renderFields();
        this.renderChips();
        this.updateFieldCounter();
        this.updateFieldsInterval();
        this.updateNoFiltersHint();
        this.updateCode();
    },

    /**
     * Add a new filter row
     */
    addFilter() {
        const template = this.elements.filterTemplate.content.cloneNode(true);
        const row = template.querySelector('.filter');
        const filterId = Date.now() + Math.random();

        const filter = {
            id: filterId,
            field: '',
            operator: '>',
            value: '',
            value2: '',
            interval: '',
            format: ''
        };
        this.state.filters.push(filter);

        const operatorSelect = row.querySelector('.filter-operator');
        const valueInput = row.querySelector('.filter-value');
        const value2Input = row.querySelector('.filter-value2');
        const removeBtn = row.querySelector('.filter-remove');
        const intervalSelect = row.querySelector('.filter-interval');
        this.populateTimeframes(intervalSelect);

        const picker = FieldPicker.create({
            getFields: () => this.getFields(),
            pinned: this.commonFilterFields,
            placeholder: 'Choose field',
            onChange: (field) => {
                filter.field = field ? field.name : '';
                filter.format = field ? field.format : '';
                if (!this.syncIntervalSelect(intervalSelect, field)) filter.interval = '';
                this.updateCode();
                valueInput.focus();
            }
        });
        row.querySelector('.filter-field').prepend(picker.el);

        intervalSelect.addEventListener('change', () => {
            filter.interval = intervalSelect.value;
            this.updateCode();
        });

        const syncOperator = () => {
            const op = operatorSelect.value;
            row.dataset.direction = op.startsWith('>') ? 'up' : op.startsWith('<') ? 'down' : 'flat';
            const between = op === 'between';
            value2Input.hidden = !between;
            row.classList.toggle('filter-range', between);
            const list = op === 'isin' || op === 'not_in';
            valueInput.placeholder = between ? 'Min' : list ? 'a, b, c' : 'Value';
        };

        operatorSelect.addEventListener('change', () => {
            filter.operator = operatorSelect.value;
            syncOperator();
            this.updateCode();
        });
        valueInput.addEventListener('input', () => {
            filter.value = valueInput.value;
            this.updateCode();
        });
        value2Input.addEventListener('input', () => {
            filter.value2 = value2Input.value;
            this.updateCode();
        });
        removeBtn.addEventListener('click', () => {
            row.remove();
            this.state.filters = this.state.filters.filter(f => f.id !== filterId);
            this.updateCode();
            this.updateNoFiltersHint();
        });

        syncOperator();
        this.elements.filtersContainer.appendChild(row);
        this.updateNoFiltersHint();
        picker.el.click();
    },

    /**
     * Update no filters hint visibility
     */
    updateNoFiltersHint() {
        this.elements.noFilters.hidden = this.elements.filtersContainer.children.length > 0;
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

        this.afterSelectionChange();
    },

    /**
     * Select all fields
     */
    selectAllFields() {
        this.state.selectAll = true;
        this.state.selectedFields = [];
        this.afterSelectionChange();
    },

    /**
     * Clear all selected fields
     */
    clearAllFields() {
        this.state.selectAll = false;
        this.state.selectedFields = [];
        this.afterSelectionChange();
    },

    /**
     * Apply a preset
     */
    applyPreset(presetName) {
        const preset = (this.presets[this.state.screenerType] || {})[presetName];
        if (!preset) return;
        this.state.selectAll = false;
        this.state.selectedFields = preset.filter(name => this.findField(name));
        this.afterSelectionChange();
    },

    afterSelectionChange() {
        this.syncCheckboxes();
        this.renderChips();
        this.updateFieldCounter();
        this.updateFieldsInterval();
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
            sortInterval: this.state.sortInterval,
            fieldsInterval: this.state.fieldsInterval,
            markets: this.state.markets,
            sortOrder: this.state.sortOrder,
            limit: this.state.limit
        };

        const lines = CodeGenerator.generateLines(config);
        this.code = lines.map(l => l.text).join('\n');
        this.renderCode(lines);
    },

    /**
     * Render highlighted code lines; lines absent from the previous render are flagged as new
     */
    renderCode(lines) {
        const previous = this.previousLines;
        const remaining = new Map();
        if (previous) {
            for (const t of previous) remaining.set(t, (remaining.get(t) || 0) + 1);
        }

        const container = this.elements.generatedCode;
        const fragment = document.createDocumentFragment();
        lines.forEach((line, i) => {
            const row = document.createElement('div');
            row.className = 'line';
            if (line.section) row.dataset.section = line.section;

            const left = remaining.get(line.text) || 0;
            if (left > 0) {
                remaining.set(line.text, left - 1);
            } else if (previous && line.text.trim()) {
                row.classList.add('fresh');
            }

            const num = document.createElement('span');
            num.className = 'ln';
            num.textContent = i + 1;

            const src = document.createElement('span');
            src.className = 'src';
            src.innerHTML = line.text
                ? hljs.highlight(line.text, { language: 'python', ignoreIllegals: true }).value
                : ' ';

            row.append(num, src);
            fragment.appendChild(row);
        });

        container.innerHTML = '';
        container.appendChild(fragment);
        this.previousLines = lines.map(l => l.text);
    },

    /**
     * Copy code to clipboard
     */
    async copyCode() {
        const btn = this.elements.copyBtn;
        const label = btn.querySelector('.copy-label');
        try {
            await navigator.clipboard.writeText(this.code);
            btn.classList.add('copied');
            label.textContent = 'Copied';
        } catch (err) {
            console.error('Failed to copy:', err);
            btn.classList.add('copy-failed');
            label.textContent = 'Copy blocked. Select the code instead.';
        }
        clearTimeout(this.copyTimer);
        this.copyTimer = setTimeout(() => {
            btn.classList.remove('copied', 'copy-failed');
            label.textContent = 'Copy code';
        }, 2000);
    }
};

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => App.init());
