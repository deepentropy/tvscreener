/**
 * Searchable field picker (combobox) used by filters and sort
 */

const FieldPicker = {
    MAX_RESULTS: 200,
    open: null,

    /**
     * Create a picker
     * @param {Object} opts
     * @param {Function} opts.getFields - Returns the field list of the current screener
     * @param {Array<string>} opts.pinned - Field names listed first when the search is empty
     * @param {string} opts.placeholder - Text shown when nothing is selected
     * @param {boolean} opts.clearable - Adds a "none" entry
     * @param {Function} opts.onChange - Called with the selected field (or null)
     * @returns {{el: HTMLElement, setValue: Function, getValue: Function}}
     */
    create(opts) {
        const el = document.createElement('button');
        el.type = 'button';
        el.className = 'picker';
        el.setAttribute('aria-haspopup', 'listbox');
        el.setAttribute('aria-expanded', 'false');

        let value = null;

        const render = () => {
            el.innerHTML = '';
            const label = document.createElement('span');
            label.className = value ? 'picker-value' : 'picker-placeholder';
            label.textContent = value ? value.label : opts.placeholder;
            const caret = document.createElement('span');
            caret.className = 'picker-caret';
            caret.setAttribute('aria-hidden', 'true');
            el.append(label, caret);
            el.title = value ? `${value.label} (${value.name})` : '';
        };

        const picker = {
            el,
            getValue: () => value,
            setValue(field) {
                value = field;
                render();
            }
        };

        el.addEventListener('click', () => {
            if (FieldPicker.open?.owner === picker) {
                FieldPicker.close();
            } else {
                FieldPicker.show(picker, opts, field => {
                    picker.setValue(field);
                    opts.onChange(field);
                });
            }
        });

        render();
        return picker;
    },

    /**
     * Open the popover under a picker
     */
    show(owner, opts, select) {
        this.close();

        const pop = document.createElement('div');
        pop.className = 'picker-pop';

        const search = document.createElement('input');
        search.type = 'search';
        search.className = 'input picker-search';
        search.placeholder = 'Search fields';
        search.autocomplete = 'off';
        search.setAttribute('aria-label', 'Search fields');

        const list = document.createElement('div');
        list.className = 'picker-list';
        list.setAttribute('role', 'listbox');

        const note = document.createElement('p');
        note.className = 'picker-note';

        pop.append(search, list, note);
        document.body.appendChild(pop);

        let items = [];
        let active = 0;

        const setActive = (i) => {
            if (!items.length) return;
            active = Math.max(0, Math.min(items.length - 1, i));
            items.forEach((it, j) => it.el.classList.toggle('active', j === active));
            items[active].el.scrollIntoView({ block: 'nearest' });
        };

        const choose = (field) => {
            this.close();
            owner.el.focus();
            select(field);
        };

        const fill = () => {
            const term = FieldSearch.normalize(search.value);
            const matches = FieldSearch.search(opts.getFields(), term, opts.pinned || []);

            list.innerHTML = '';
            items = [];

            const entries = matches.slice(0, this.MAX_RESULTS);
            if (opts.clearable && !term) entries.unshift(null);

            for (const field of entries) {
                const row = document.createElement('div');
                row.className = 'picker-item';
                row.setAttribute('role', 'option');
                if (field) {
                    const l = document.createElement('span');
                    l.className = 'picker-item-label';
                    l.textContent = field.label;
                    const n = document.createElement('span');
                    n.className = 'picker-item-name';
                    n.textContent = field.name;
                    row.append(l, n);
                    if (owner.getValue()?.name === field.name) row.setAttribute('aria-selected', 'true');
                } else {
                    row.classList.add('picker-item-none');
                    row.textContent = 'Default order';
                }
                row.addEventListener('mousedown', e => e.preventDefault());
                row.addEventListener('click', () => choose(field));
                row.addEventListener('mousemove', () => {
                    const i = items.findIndex(it => it.el === row);
                    if (i !== active) setActive(i);
                });
                list.appendChild(row);
                items.push({ el: row, field });
            }

            if (!matches.length) {
                note.textContent = `No field matches "${search.value.trim()}".`;
            } else if (matches.length > this.MAX_RESULTS) {
                note.textContent = `${this.MAX_RESULTS} of ${matches.length.toLocaleString('en-US')} shown. Type to narrow.`;
            } else {
                note.textContent = '';
            }
            active = 0;
            setActive(0);
        };

        search.addEventListener('input', fill);
        search.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowDown') { e.preventDefault(); setActive(active + 1); }
            else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(active - 1); }
            else if (e.key === 'Enter') { e.preventDefault(); if (items[active]) choose(items[active].field); }
            else if (e.key === 'Escape') { e.preventDefault(); this.close(); owner.el.focus(); }
            else if (e.key === 'Tab') { this.close(); }
        });

        this.open = { owner, pop };
        owner.el.setAttribute('aria-expanded', 'true');
        this.position();
        fill();
        search.focus();
    },

    /**
     * Place the popover under its trigger, or above when there is no room
     */
    position() {
        if (!this.open) return;
        const { owner, pop } = this.open;
        const r = owner.el.getBoundingClientRect();
        const width = Math.max(r.width, 360);
        const left = Math.min(r.left, window.innerWidth - width - 8);
        pop.style.width = `${width}px`;
        pop.style.left = `${Math.max(8, left)}px`;
        const below = window.innerHeight - r.bottom;
        if (below < 280 && r.top > below) {
            pop.style.top = '';
            pop.style.bottom = `${window.innerHeight - r.top + 4}px`;
        } else {
            pop.style.bottom = '';
            pop.style.top = `${r.bottom + 4}px`;
        }
    },

    close() {
        if (!this.open) return;
        this.open.owner.el.setAttribute('aria-expanded', 'false');
        this.open.pop.remove();
        this.open = null;
    }
};

document.addEventListener('mousedown', (e) => {
    const o = FieldPicker.open;
    if (o && !o.pop.contains(e.target) && !o.owner.el.contains(e.target)) FieldPicker.close();
});
window.addEventListener('resize', () => FieldPicker.position());
document.addEventListener('scroll', () => FieldPicker.position(), true);
