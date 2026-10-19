const fs = require('fs');
const {familyMembers, ancestor, descendants} = require('../solution/solution.js');

const workdir = '../workdir';

function randint(start, end) {
    return Math.floor(Math.random() * (end - start)) + start;
}

function shuffle(array) {
    let currentIndex = array.length, temporaryValue, randomIndex;

    // While there remain elements to shuffle...
    while (0 !== currentIndex) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
}

function choice(array) {
    return array[Math.floor(Math.random() * array.length)];
}

function familyGenerator(males, females, maxChildren = 5, maxGenerations = 5) {
    const malesList = [...males];
    const femalesList = [...females];
    const family = [];

    function generateFamily(father = null, mother = null, offSpringOdds = 1.0) {
        father = father || malesList.splice(Math.floor(Math.random() * malesList.length), 1);
        mother = mother || femalesList.splice(Math.floor(Math.random() * femalesList.left), 1);
        const children = [father, mother];
        [...Array(randint(1, maxChildren)).keys()].forEach(() => {
            children.push(randint(0, 1) === 1 ?
                malesList.splice(Math.floor(Math.random() * malesList.length), 1) :
                femalesList.splice(Math.floor(Math.random() * femalesList.left), 1));
        });
        family.push(children);
        for (let child of children.slice(2)) {
            if (Math.random() < offSpringOdds) {
                if (males.indexOf(child) !== -1) {
                    generateFamily(child, null, offSpringOdds - 1 / maxGenerations);
                } else {
                    generateFamily(null, child, offSpringOdds - 1 / maxGenerations);
                }
            }
        }
    }

    generateFamily();
    return shuffle(family);
}

const females = fs.readFileSync('male_names.txt')
    .toString()
    .split('\n')
    .map(s => s.trim())
    .filter(s => s.search(/^[A-Z]+$/i) === 0);
const males = fs.readFileSync('male_names.txt')
    .toString()
    .split('\n')
    .map(s => s.trim())
    .filter(s => s.search(/^[A-Z]+$/i) === 0)
    .filter(s => females.indexOf(s) !== -1);

function flow(value) {
    if (Array.isArray(value)) {
        return `[${value.map(flow).join(', ')}]`;
    }
    if (typeof value === 'object') {
        return `{${Object.entries(value).map(([k, v]) => `${JSON.stringify(k)}: ${flow(v)}`).join(', ')}}`;
    }
    return JSON.stringify(value);
}

const famContexts = [];
const voContexts = [];
const naContexts = [];

[...Array(50).keys()].map(i => i + 1).forEach((i) => {
    const maxGenerations = 2 + Math.floor(i / 20);
    const maxChildren = 5 - Math.floor(i / 20);
    const family = familyGenerator(males, females, maxChildren, maxGenerations);
    fs.writeFileSync(`${workdir}/data${i}.txt`, family.map(a => a.join(' ')).join('\n'));

    const allNames = family.flat(2);
    const load = [
        '      - testcases:',
        `          - statement: 'relations${i}: object = familyMembers("data${i}.txt")'`
    ];

    famContexts.push(...load);
    const famOpl = familyMembers(`${workdir}/data${i}.txt`);
    [...Array(5).keys()].forEach(() => {
        const person = choice(allNames);
        famContexts.push(
            '          - expression:',
            `              javascript: 'relations${i}["${person}"]'`,
            `            return: !object ${flow(famOpl[person])}`
        );
    });

    voContexts.push(...load);
    let person = choice(allNames);
    const relatie = [...Array(randint(1, 2 + Math.floor(i / 20))).keys()]
        .map(() => choice(['mor', 'far']))
        .join('');
    let voOpl;
    try {
        voOpl = `            return: ${flow(ancestor(person, relatie, famOpl))}`;
    } catch (e) {
        voOpl = '            exception: *unknown_ancestor';
    }
    voContexts.push(`          - expression: 'ancestor("${person}", "${relatie}", relations${i})'`, voOpl);

    naContexts.push(...load);
    person = choice(allNames);
    let generation = randint(1, 3);
    let naOpl = descendants(person, generation, famOpl);
    while (Object.keys(naOpl).length === 0) {
        person = choice(allNames);
        generation = randint(1, 3);
        naOpl = descendants(person, generation, famOpl);
    }
    naContexts.push(
        `          - expression: 'descendants("${person}", ${generation}, relations${i})'`,
        `            return: !object ${flow(naOpl)}`
    );
});

const suite = [
    'definitions:',
    '  unknown_ancestor: &unknown_ancestor',
    '    message: "unknown ancestor"',
    '    types:',
    '      javascript: "AssertionError"',
    'tabs:',
    '  - tab: "familyMembers"',
    '    contexts:',
    ...famContexts,
    '  - tab: "ancestor"',
    '    contexts:',
    ...voContexts,
    '  - tab: "descendants"',
    '    contexts:',
    ...naContexts
];

fs.writeFileSync('../evaluation/suite.yaml', suite.join('\n') + '\n');
