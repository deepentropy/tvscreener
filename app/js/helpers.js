/**
 * tvscreener Code Generator - Helpers mode
 * Builds the call of one tvscreener helper function (financials, calendars, news...) from a form.
 */

const DOCS = 'https://deepentropy.github.io/tvscreener/docs';

const isoDay = (offset = 0) => {
    const d = new Date();
    d.setDate(d.getDate() + offset);
    return d.toISOString().slice(0, 10);
};

// Monthly option expiration: third Friday of the month after next
const monthlyExpiration = () => {
    const d = new Date();
    d.setDate(1);
    d.setMonth(d.getMonth() + 1);
    d.setDate(1 + ((5 - d.getDay() + 7) % 7) + 14);
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
};

// Reusable parameter definitions
const P = {
    symbol: (value = 'NASDAQ:AAPL') => ({ name: 'symbol', label: 'Symbol', type: 'text', value, required: true, positional: true }),
    start: (value = '') => ({ name: 'start', label: 'Start', type: 'date', value }),
    end: (value = '') => ({ name: 'end', label: 'End', type: 'date', value }),
    markets: () => ({ name: 'markets', label: 'Markets', type: 'list', value: '', placeholder: 'america, germany (default america)' })
};

/**
 * Helper functions. Parameter types:
 *   text, number, date: one value; list: comma-separated values sent as a Python list;
 *   select: options; multi: checkboxes sent as a list; checkbox: bool; varargs: comma-separated positional args.
 * An argument is left out when it is empty or equal to its Python default (pyDefault).
 * render(call) returns the code lines that use the call.
 */
const HELPERS = [
    // ---- Company ----
    {
        fn: 'get_financials', group: 'Company', label: 'Financials',
        desc: 'Income statement, balance sheet, cash flow or ratios: about 20 years and 32 quarters.',
        doc: `${DOCS}/guide/fundamentals/#financial-statements`,
        params: [
            P.symbol(),
            { name: 'statement', label: 'Statement', type: 'select', value: 'income', pyDefault: 'income',
              options: [['income', 'Income statement'], ['balance_sheet', 'Balance sheet'], ['cash_flow', 'Cash flow'], ['statistics', 'Statistics']] },
            { name: 'period', label: 'Period', type: 'select', value: 'FY', pyDefault: 'FY',
              options: [['FY', 'Annual'], ['FQ', 'Quarterly'], ['FH', 'Semi-annual'], ['TTM', 'Trailing 12 months']] },
            { name: 'labels', label: 'Readable names', type: 'checkbox', value: true, pyDefault: true }
        ],
        render: call => [`df = ${call}`, 'print(df.attrs["currency"])', 'print(df.tail())']
    },
    {
        fn: 'get_corporate_events', group: 'Company', label: 'Dividends, earnings, splits',
        desc: 'Recent dividends, earnings releases (actual vs estimate, next date) and stock splits.',
        doc: `${DOCS}/guide/fundamentals/#corporate-events`,
        params: [
            P.symbol(),
            { name: 'kinds', label: 'Events', type: 'multi', value: ['dividends', 'earnings', 'splits'],
              pyDefault: ['dividends', 'earnings', 'splits'],
              options: [['dividends', 'Dividends'], ['earnings', 'Earnings'], ['splits', 'Splits']] }
        ],
        render: (call, v) => [`events = ${call}`, ...(v.kinds.length ? v.kinds : ['dividends', 'earnings', 'splits']).map(k => `print(events["${k}"])`)]
    },
    {
        fn: 'get_seasonals', group: 'Company', label: 'Seasonals',
        desc: 'Monthly returns, one row per year.',
        doc: `${DOCS}/guide/fundamentals/#seasonals`,
        params: [
            P.symbol(),
            { name: 'start_year', label: 'From year', type: 'number', value: '', placeholder: '10 years by default' },
            { name: 'end_year', label: 'To year', type: 'number', value: '', placeholder: 'Current year' },
            { name: 'absolute', label: 'Price change', type: 'checkbox', value: false, pyDefault: false }
        ],
        render: call => [`df = ${call}`, 'print(df)', 'print(df.mean())  # average by month']
    },
    {
        fn: 'get_peers', group: 'Company', label: 'Peers',
        desc: 'Largest companies of the same industry or sector, in the same market.',
        doc: `${DOCS}/guide/scanner-helpers/#peers`,
        params: [
            P.symbol(),
            { name: 'n', label: 'Peers', type: 'number', value: 10, pyDefault: 10 },
            { name: 'by', label: 'Same', type: 'select', value: 'industry', pyDefault: 'industry',
              options: [['industry', 'Industry'], ['sector', 'Sector']] }
        ],
        render: call => [`df = ${call}`, 'print(df)']
    },
    {
        fn: 'get_symbol', group: 'Company', label: 'Symbol fields',
        desc: 'Any scanner fields of one symbol, as a dict.',
        doc: `${DOCS}/guide/scanner-helpers/#one-symbol`,
        params: [
            P.symbol(),
            { name: 'fields', label: 'Fields', type: 'varargs', value: 'close, market_cap_basic, RSI, price_earnings_ttm', required: true }
        ],
        render: call => [`data = ${call}`, 'print(data)']
    },

    // ---- Live ----
    {
        fn: 'stream_quotes', group: 'Live', label: 'Real-time quotes',
        desc: 'Quotes pushed by TradingView as they change, including pre/after-market prices.',
        doc: `${DOCS}/guide/streaming/#real-time-quotes`,
        params: [
            { name: 'symbols', label: 'Symbols', type: 'list', value: 'NASDAQ:AAPL, BINANCE:BTCUSDT', required: true, positional: true },
            { name: 'fields', label: 'Fields', type: 'list', value: '', placeholder: 'price, bid, ask, volume (default set)' },
            { name: 'duration', label: 'Seconds', type: 'number', value: 60 },
            { name: 'max_updates', label: 'Max updates', type: 'number', value: '' }
        ],
        render: call => [`for quote in ${call}:`, '    print(quote["symbol"], quote.get("price"), quote["updated"])']
    },

    // ---- Calendars ----
    {
        fn: 'get_economic_calendar', group: 'Calendars', label: 'Economic',
        desc: 'Data releases, central bank decisions and speeches, with actual, forecast and previous values.',
        doc: `${DOCS}/guide/presets-calendars/#economic-events`,
        params: [
            P.start(isoDay(0)), P.end(isoDay(7)),
            { name: 'countries', label: 'Countries', type: 'list', value: 'US, EU', placeholder: 'All countries' },
            { name: 'importance', label: 'Importance', type: 'select', value: '', pyDefault: '',
              options: [['', 'All'], ['low', 'Low and above'], ['medium', 'Medium and above'], ['high', 'High']] }
        ],
        render: call => [`df = ${call}`, 'print(df[["date", "country", "title", "actual", "forecast", "previous"]])']
    },
    ...[['get_earnings_calendar', 'Earnings', 'Earnings releases with estimates, and actual values once reported.', 'earnings'],
        ['get_dividends_calendar', 'Dividends', 'Dividends by ex-dividend date.', 'dividends'],
        ['get_ipo_calendar', 'IPOs', 'IPOs by offer date.', 'ipos']].map(([fn, label, desc, anchor]) => ({
        fn, group: 'Calendars', label, desc,
        doc: `${DOCS}/guide/presets-calendars/#${anchor}`,
        params: [P.start(isoDay(0)), P.end(isoDay(7)), P.markets()],
        render: call => [`df = ${call}`, 'print(df)']
    })),

    // ---- News and filings ----
    {
        fn: 'get_news', group: 'News & filings', label: 'News',
        desc: 'Latest headlines (up to 200). Filters are combined with AND.',
        doc: `${DOCS}/guide/news-documents/#news`,
        params: [
            { name: 'symbol', label: 'Symbol', type: 'text', value: 'NASDAQ:AAPL', placeholder: 'All news', positional: true },
            { name: 'provider', label: 'Provider', type: 'select', value: '', pyDefault: '',
              options: [['', 'Any'], ['reuters', 'Reuters'], ['dow-jones', 'Dow Jones'], ['business_wire', 'Business Wire'],
                        ['tradingview', 'TradingView'], ['zacks', 'Zacks'], ['benzinga', 'Benzinga'], ['marketbeat', 'MarketBeat']] },
            { name: 'market', label: 'Market', type: 'select', value: '', pyDefault: '',
              options: [['', 'Any'], ['stock', 'Stocks'], ['etf', 'ETFs'], ['crypto', 'Crypto'], ['forex', 'Forex'],
                        ['index', 'Indices'], ['futures', 'Futures'], ['bond', 'Bonds'], ['economic', 'Economy']] },
            { name: 'corp_activity', label: 'Activity', type: 'select', value: '', pyDefault: '',
              options: [['', 'Any'], ['earnings', 'Earnings'], ['dividends', 'Dividends'], ['insider_trading', 'Insider trading'],
                        ['recommendation', 'Analyst ratings'], ['mergers_and_acquisitions', 'M&A'], ['share_buybacks', 'Buybacks'],
                        ['ipo', 'IPO'], ['management', 'Management'], ['esg', 'ESG'], ['credit_ratings', 'Credit ratings']] },
            { name: 'country', label: 'Country', type: 'text', value: '', placeholder: 'e.g. US' },
            { name: 'priority', label: 'Priority', type: 'select', value: '', pyDefault: '',
              options: [['', 'Any'], ['important', 'Important'], ['top_stories', 'Top stories'], ['flash', 'Flash'], ['key_facts', 'Key facts']] }
        ],
        render: call => [`news = ${call}`, 'print(news[["published", "title", "provider"]])', '',
                         '# Full text of the latest story', 'print(tvs.get_article(news["id"].iloc[0]))']
    },
    {
        fn: 'get_documents', group: 'News & filings', label: 'Filings & transcripts',
        desc: '10-Q, 10-K, earnings releases, call and event transcripts.',
        doc: `${DOCS}/guide/news-documents/#filings-and-transcripts`,
        params: [
            P.symbol(),
            { name: 'category', label: 'Category', type: 'multi', value: ['call_transcript'], pyDefault: [],
              options: [['quarterly_report', '10-Q / quarterly'], ['annual_report', '10-K / annual'], ['earnings_release', 'Earnings release'],
                        ['call_transcript', 'Call transcript'], ['event_transcript', 'Event transcript'], ['slides', 'Slides']] },
            P.start(), P.end()
        ],
        render: (call, v) => {
            const lines = [`docs = ${call}`, 'print(docs[["date", "title", "category", "form"]])'];
            const transcripts = !v.category.length || v.category.some(c => c.endsWith('transcript'));
            if (transcripts) {
                lines.push('', '# Text of the latest transcript', 'print(tvs.get_document(docs["transcript_id"].dropna().iloc[0]))');
            }
            return lines;
        }
    },
    {
        fn: 'get_earnings_calls', group: 'News & filings', label: 'Earnings calls',
        desc: 'Past and scheduled earnings calls, with transcript and recording links.',
        doc: `${DOCS}/guide/news-documents/#earnings-calls`,
        params: [P.symbol(), P.start(), P.end()],
        render: call => [`calls = ${call}`, 'print(calls[["date", "title", "state", "audio_url"]])']
    },

    // ---- Markets ----
    {
        fn: 'search_symbols', group: 'Markets', label: 'Symbol search',
        desc: 'Find exchange-prefixed symbols by ticker, name, ISIN or CUSIP.',
        doc: `${DOCS}/guide/scanner-helpers/#symbol-search`,
        params: [
            { name: 'text', label: 'Search', type: 'text', value: 'apple', required: true, positional: true },
            { name: 'type', label: 'Type', type: 'select', value: '', pyDefault: '',
              options: [['', 'Any'], ['stock', 'Stocks'], ['funds', 'Funds'], ['futures', 'Futures'], ['forex', 'Forex'],
                        ['crypto', 'Crypto'], ['index', 'Indices'], ['bond', 'Bonds'], ['economic', 'Economy']] },
            { name: 'exchange', label: 'Exchange', type: 'text', value: '', placeholder: 'e.g. NASDAQ' },
            { name: 'country', label: 'Country', type: 'text', value: '', placeholder: 'Listings first, e.g. DE' },
            { name: 'limit', label: 'Results', type: 'number', value: 50, pyDefault: 50 }
        ],
        render: call => [`df = ${call}`, 'print(df[["symbol", "description", "type", "exchange", "isin"]])']
    },
    {
        fn: 'get_forward_curve', group: 'Markets', label: 'Futures curve',
        desc: 'Every listed contract month of a futures root, by expiration.',
        doc: `${DOCS}/screeners/futures/#forward-curve`,
        params: [{ name: 'root', label: 'Root', type: 'text', value: 'NYMEX:CL', required: true, positional: true }],
        render: call => [`df = ${call}`, 'print(df[["symbol", "expiration", "close", "open_interest"]])']
    },
    {
        fn: 'get_yield_curve', group: 'Markets', label: 'Yield curve',
        desc: 'Government bond yields of one country, by tenor.',
        doc: `${DOCS}/screeners/government-bonds/#yield-curve`,
        params: [{ name: 'country', label: 'Country', type: 'text', value: 'US', required: true, positional: true }],
        render: call => [`df = ${call}`, 'print(df[["tenor", "yield", "change"]])']
    },
    {
        fn: 'get_yield_matrix', group: 'Markets', label: 'Yield matrix',
        desc: 'Government bond yields of several countries side by side.',
        doc: `${DOCS}/screeners/government-bonds/#yield-matrix`,
        params: [
            { name: 'countries', label: 'Countries', type: 'list', value: 'US, DE, JP, GB', placeholder: 'All countries', positional: true },
            { name: 'tenors', label: 'Tenors', type: 'list', value: '2Y, 10Y, 30Y', placeholder: 'All tenors' }
        ],
        render: call => [`df = ${call}`, 'print(df)']
    },
    {
        fn: 'get_volatility_smile', group: 'Markets', label: 'Volatility smile',
        desc: 'Implied volatility of one option expiration, by strike or moneyness.',
        doc: `${DOCS}/screeners/option/#volatility-smile`,
        params: [
            P.symbol(),
            { name: 'expiration', label: 'Expiration', type: 'date', value: monthlyExpiration(), required: true, positional: true },
            { name: 'root', label: 'Option root', type: 'text', value: '', placeholder: 'Ticker by default, e.g. SPXW' },
            { name: 'x', label: 'X axis', type: 'select', value: 'strike', pyDefault: 'strike',
              options: [['strike', 'Strike'], ['moneyness', 'Moneyness']] }
        ],
        render: call => [`df = ${call}`, 'print(df)']
    },
    {
        fn: 'get_iv_term_structure', group: 'Markets', label: 'IV term structure',
        desc: 'Implied volatility by time to expiration.',
        doc: `${DOCS}/screeners/option/#iv-term-structure`,
        params: [P.symbol()],
        render: call => [`df = ${call}`, 'print(df)']
    }
];

const HelperGenerator = {
    py(value) {
        if (typeof value === 'boolean') return value ? 'True' : 'False';
        if (typeof value === 'number') return String(value);
        return JSON.stringify(String(value));
    },

    splitList(text) {
        return String(text || '').split(',').map(s => s.trim()).filter(Boolean);
    },

    /**
     * Python value of a parameter, or null when the argument is left out
     */
    argValue(param, value) {
        const same = (a, b) => JSON.stringify(a) === JSON.stringify(b);
        const normalized = param.type === 'number' && value !== '' && value !== null ? Number(value) : value;
        if ('pyDefault' in param && same(normalized, param.pyDefault)) return null;
        switch (param.type) {
            case 'checkbox':
                return this.py(Boolean(value));
            case 'number': {
                const n = Number(value);
                return value === '' || value === null || Number.isNaN(n) ? null : String(n);
            }
            case 'list': {
                const items = this.splitList(value);
                return items.length ? `[${items.map(i => this.py(i)).join(', ')}]` : null;
            }
            case 'multi':
                return value.length ? `[${value.map(i => this.py(i)).join(', ')}]` : null;
            default:
                return String(value || '').trim() ? this.py(String(value).trim()) : null;
        }
    },

    /**
     * Code lines for a helper and its form values
     * @returns {Array<{text: string, section: string|null}>}
     */
    generateLines(helper, values) {
        const args = [];
        let keyword = false;
        for (const param of helper.params) {
            if (param.type === 'varargs') {
                args.push(...this.splitList(values[param.name]).map(f => this.py(f)));
                continue;
            }
            const value = this.argValue(param, values[param.name]);
            if (value === null) {
                // Later positional arguments would shift: switch to keywords
                keyword = true;
                continue;
            }
            const positional = param.positional && !keyword;
            if (!positional) keyword = true;
            args.push(positional ? value : `${param.name}=${value}`);
        }

        let call = `tvs.${helper.fn}(${args.join(', ')})`;
        if (call.length > 88 && args.length > 1) {
            call = `tvs.${helper.fn}(\n    ${args.join(',\n    ')},\n)`;
        }

        const lines = [
            { text: 'import tvscreener as tvs', section: 'helper' },
            { text: '', section: null }
        ];
        for (const block of helper.render(call, values)) {
            for (const text of block.split('\n')) lines.push({ text, section: 'args' });
        }
        return lines;
    }
};

const HelperPanel = {
    current: HELPERS[0].fn,
    values: {},

    init(onChange) {
        this.onChange = onChange;
        this.list = document.getElementById('helper-list');
        this.form = document.getElementById('helper-form');
        this.desc = document.getElementById('helper-desc');
        this.docLink = document.getElementById('helper-doc');
        this.title = document.getElementById('helper-args-title');
        for (const helper of HELPERS) {
            this.values[helper.fn] = Object.fromEntries(helper.params.map(p => [p.name, structuredClone(p.value)]));
        }
        this.renderList();
        this.select(this.current);
    },

    helper() {
        return HELPERS.find(h => h.fn === this.current);
    },

    count() {
        return HELPERS.length;
    },

    renderList() {
        this.list.innerHTML = '';
        const groups = [...new Set(HELPERS.map(h => h.group))];
        for (const group of groups) {
            const row = document.createElement('div');
            row.className = 'presets helper-group';
            const label = document.createElement('span');
            label.className = 'presets-label';
            label.textContent = group;
            const pills = document.createElement('div');
            pills.className = 'presets-list';
            for (const helper of HELPERS.filter(h => h.group === group)) {
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = 'preset helper-pill';
                btn.dataset.fn = helper.fn;
                btn.textContent = helper.label;
                btn.title = `${helper.fn}()`;
                btn.addEventListener('click', () => this.select(helper.fn));
                pills.appendChild(btn);
            }
            row.append(label, pills);
            this.list.appendChild(row);
        }
    },

    select(fn) {
        this.current = fn;
        const helper = this.helper();
        this.list.querySelectorAll('.helper-pill').forEach(b => {
            const on = b.dataset.fn === fn;
            b.classList.toggle('active', on);
            b.setAttribute('aria-pressed', String(on));
        });
        this.desc.textContent = helper.desc;
        this.docLink.href = helper.doc;
        this.title.textContent = `${helper.fn}()`;
        this.renderForm();
        this.onChange();
    },

    renderForm() {
        const helper = this.helper();
        const values = this.values[helper.fn];
        this.form.innerHTML = '';

        for (const param of helper.params) {
            const row = document.createElement(param.type === 'multi' ? 'div' : 'label');
            row.className = 'option';
            const label = document.createElement('span');
            label.className = 'option-label';
            label.textContent = param.label;
            row.appendChild(label);

            let control;
            if (param.type === 'select') {
                control = document.createElement('select');
                control.className = 'input select';
                for (const [value, text] of param.options) {
                    const option = document.createElement('option');
                    option.value = value;
                    option.textContent = text;
                    control.appendChild(option);
                }
                control.value = values[param.name];
                control.addEventListener('change', () => this.set(param.name, control.value));
            } else if (param.type === 'checkbox') {
                control = document.createElement('input');
                control.type = 'checkbox';
                control.className = 'helper-check';
                control.checked = values[param.name];
                control.addEventListener('change', () => this.set(param.name, control.checked));
            } else if (param.type === 'multi') {
                control = document.createElement('div');
                control.className = 'helper-multi';
                for (const [value, text] of param.options) {
                    const item = document.createElement('label');
                    item.className = 'helper-multi-item';
                    const box = document.createElement('input');
                    box.type = 'checkbox';
                    box.checked = values[param.name].includes(value);
                    box.addEventListener('change', () => {
                        const chosen = param.options.map(o => o[0]).filter(v =>
                            v === value ? box.checked : values[param.name].includes(v));
                        this.set(param.name, chosen);
                    });
                    item.append(box, document.createTextNode(text));
                    control.appendChild(item);
                }
            } else {
                control = document.createElement('input');
                control.type = param.type === 'number' ? 'number' : param.type === 'date' ? 'date' : 'text';
                control.className = 'input' + (param.type === 'number' ? ' input-num' : '');
                control.value = values[param.name];
                control.placeholder = param.placeholder || (param.type === 'list' || param.type === 'varargs' ? 'a, b, c' : '');
                control.spellcheck = false;
                control.autocomplete = 'off';
                control.addEventListener('input', () => this.set(param.name, control.value));
            }
            row.appendChild(control);
            this.form.appendChild(row);
        }
    },

    set(name, value) {
        this.values[this.current][name] = value;
        this.onChange();
    },

    generateLines() {
        return HelperGenerator.generateLines(this.helper(), this.values[this.current]);
    }
};
