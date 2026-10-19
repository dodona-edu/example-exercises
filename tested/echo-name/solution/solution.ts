import * as fs from "fs";

const name = fs.readFileSync(0, "utf8").split("\n")[0];
console.log(`Hallo, ${name}!`);
