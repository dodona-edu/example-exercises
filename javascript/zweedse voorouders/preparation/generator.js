const fs = require('fs');
const {familieleden, voorouder, nakomelingen} = require('../solution/solution.nl.js');

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

const famStatements = ['judge.config("switch-tab", "familieleden");'];
const voStatements = ['judge.config("switch-tab", "voorouder");'];
const naStatements = ['judge.config("switch-tab", "nakomelingen");'];

[...Array(50).keys()].map(i => i + 1).forEach((i) => {
    const maxGenerations = 2 + Math.floor(i / 20);
    const maxChildren = 5 - Math.floor(i / 20);
    const family = familyGenerator(males, females, maxChildren, maxGenerations);
    fs.writeFileSync(`${workdir}/data${i}.txt`, family.map(a => a.join(' ')).join('\n'));

    const allNames = [].concat(...family);

    famStatements.push('judge.config("switch-context");');
    const famOpl = familieleden(`${workdir}/data${i}.txt`);
    famStatements.push(`judge.test('const relaties${i} = familieleden("data${i}.txt");');`);
    [...Array(5).keys()].forEach(() => {
        const person = choice(allNames);
        famStatements.push(`judge.test('relaties${i}["${person}"]', JSON.parse('${JSON.stringify(famOpl[person])}'));`);
    });

    voStatements.push('judge.config("switch-context");');
    voStatements.push(`judge.test('const relaties${i} = familieleden("data${i}.txt");');`);
    let person = choice(allNames);
    const relatie = [...Array(randint(1, 2 + Math.floor(i / 20))).keys()]
        .map(() => choice(['mor', 'far']))
        .join('');
    let voOpl = null;
    try {
        voOpl = voorouder(person, relatie, famOpl);
    } catch (e) {
        voOpl = `exception:${e}`;
    }
    voStatements.push(`judge.test('voorouder("${person}", "${relatie}", relaties${i})', '${voOpl}');`);

    naStatements.push('judge.config("switch-context");');
    naStatements.push(`judge.test('const relaties${i} = familieleden("data${i}.txt");');`);
    person = choice(allNames);
    let generation = randint(1, 3);
    let naOpl = nakomelingen(person, generation, famOpl);
    while (Object.keys(naOpl).length === 0) {
        person = choice(allNames);
        generation = randint(1, 3);
        naOpl = nakomelingen(person, generation, famOpl);
    }
    naStatements.push(`judge.test('nakomelingen("${person}", ${generation}, relaties${i})', JSON.parse('${JSON.stringify(naOpl)}'));`);


});

const statements = ['judge.config("auto-switch-context", false);']
    .concat(famStatements)
    .concat(voStatements)
    .concat(naStatements);

fs.writeFileSync('../evaluation/tests.js', statements.join('\n'));
