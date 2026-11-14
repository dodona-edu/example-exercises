// CJS require honours NODE_PATH; ESM bare imports do not.
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);
const js = require("@eslint/js");
const globals = require("globals");

// Dodona stores the submission as `source`, without an extension.
const files = ["**/!(*.*)", "**/*.js"];

export default [
  { files, ...js.configs.recommended },
  {
    files,
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "commonjs",
      globals: { ...globals.node, ...globals.es2020, prompt: "readonly" },
    },
    rules: {
      "no-var": "warn",
      semi: "warn",
      "no-unused-vars": "off",
    },
  },
];
