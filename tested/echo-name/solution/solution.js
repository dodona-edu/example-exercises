const fs = require("fs");

const naam = fs.readFileSync(0, "utf8").split("\n")[0];
console.log(`Hallo, ${naam}!`);
