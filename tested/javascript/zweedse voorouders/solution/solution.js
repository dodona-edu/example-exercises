const fs = require("fs");
const assert = require("assert");

function familyMembers(file) {
    const relations = {};
    const member = name => (relations[name] ??= {});
    for (const line of fs.readFileSync(file, "utf8").split("\n")) {
        const [mother, father, ...children] = line.trim().split(/\s+/);
        if (children.length === 0) {
            continue;
        }
        for (const parent of [mother, father]) {
            member(parent).children = [...(member(parent).children ?? []), ...children].sort();
        }
        for (const child of children) {
            member(child).mother = mother;
            member(child).father = father;
        }
    }
    return relations;
}

function ancestor(name, description, relations) {
    let person = name;
    for (const part of description.match(/mor|far/g)) {
        person = relations[person]?.[part === "mor" ? "mother" : "father"];
        assert(person !== undefined, "unknown ancestor");
    }
    return person;
}

function descendants(name, n, relations) {
    let generation = [[name, ""]];
    for (let i = 0; i < n; i++) {
        generation = generation.flatMap(([person, description]) =>
            (relations[person].children ?? []).map(child => [
                child,
                (relations[child].mother === person ? "mor" : "far") + description
            ])
        );
    }
    const result = {};
    for (const [child, description] of generation) {
        (result[description] ??= []).push(child);
    }
    for (const children of Object.values(result)) {
        children.sort();
    }
    return result;
}

module.exports = { familyMembers, ancestor, descendants };
