/**
 * Field search shared by the column list and the field picker.
 * A field matches when the term is found in its label or Python name,
 * or when the term is the start of its initials ("rsi" -> Relative Strength Index (14),
 * "sma50" -> Simple Moving Average (50)).
 */

const FieldSearch = {
    /**
     * Initials of a label; numbers are kept whole
     * "Simple Moving Average (50)" -> "sma50"
     */
    initials(field) {
        if (field._initials === undefined) {
            const words = field.label.toLowerCase().match(/[a-z]+|\d+/g) || [];
            field._initials = words.map(w => /^\d/.test(w) ? w : w[0]).join('');
        }
        return field._initials;
    },

    normalize(term) {
        return term.trim().toLowerCase();
    },

    /**
     * Rank of a field for a search term; lower is better, -1 means no match
     * 0: initials start with the term
     * 1: label starts with the term
     * 2: label or Python name contains the term
     */
    rank(field, term) {
        if (!term) return 2;
        const compact = term.replace(/[^a-z0-9]/g, '');
        if (compact.length >= 2 && this.initials(field).startsWith(compact)) return 0;
        const label = field.label.toLowerCase();
        if (label.startsWith(term)) return 1;
        if (label.includes(term) || field.name.toLowerCase().includes(term)) return 2;
        return -1;
    },

    /**
     * Fields matching a term, best matches first
     * @param {Array} fields
     * @param {string} term - Raw search text
     * @param {Array<string>} pinned - Field names ranked first inside each match rank
     */
    search(fields, term, pinned = []) {
        term = this.normalize(term);
        const ranked = [];
        for (const f of fields) {
            const r = this.rank(f, term);
            if (r >= 0) ranked.push({ f, r, p: pinned.includes(f.name) ? 0 : 1 });
        }
        ranked.sort((a, b) => (a.r - b.r) || (a.p - b.p) || a.f.label.localeCompare(b.f.label));
        return ranked.map(x => x.f);
    }
};
