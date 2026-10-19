class MadLibsError extends Error {
    constructor(message) {
        super(message);
        this.name = "MadLibsError";
    }
}

class MadLibs {
    constructor() {
        this.vocabulary = {};
    }

    learn(category, words) {
        if (!Array.isArray(words)) {
            words = [words];
        }
        category = category.toLowerCase();
        if (!Object.hasOwn(this.vocabulary, category)) {
            this.vocabulary[category] = [];
        }
        for (const word of words) {
            this.vocabulary[category].push(word.toLowerCase());
        }
    }

    suggest(category) {
        const key = category.toLowerCase();
        if (!Object.hasOwn(this.vocabulary, key)) {
            throw new MadLibsError("unknown category");
        }
        const words = this.vocabulary[key];
        let word = words[Math.floor(Math.random() * words.length)];
        if (/^[A-Z]+$/.test(category)) {
            word = word.toUpperCase();
        } else if (/^[A-Z][a-z]*$/.test(category)) {
            word = word.charAt(0).toUpperCase() + word.slice(1);
        }
        return word;
    }

    fill(text) {
        return text.replace(/_([^_]*)_/g, (_, category) => this.suggest(category));
    }
}
