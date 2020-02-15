// https://eslint.org/docs/user-guide/configuring

module.exports = {
  root: true,
  parserOptions: {
    parser: 'babel-eslint'
  },
  env: {
    browser: true,
  },
  extends: ["plugin:vue/strongly-recommended", "google"],
  // required to lint *.vue files
  plugins: [
    'vue'
  ],
  // add your custom rules here
  rules: {
    // if you forget to add a comma, the linter / compiler will yell at you.
    // If you get in the habit of adding commas everywhere, you'll break json
    // or situations where you don't use it (for example, languages that aren't
    // js).
    "comma-dangle": ["error", "never"],
    // allow async-await
    'generator-star-spacing': 'off',
    // as a rule, maximum lengths should be 100, but there are good reasons to break this rule.
    // try to keep it under 100, and definitely keep it under 120.  URLs are a notable exception.
    // comments should never be longer than 100
    "max-len": [2, 120, 2, {
      "ignoreUrls": true,
      "ignoreComments": false
    }],
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    "prefer-object-spread": ["warn"],
    "quotes": ["error", "double", "avoid-escape"],
    "space-in-parens": ["error", "never"],
    // the first attribute should appear on the same line as the opening tag
    "vue/max-attributes-per-line": [2, {
      "singleline": 99,
      "multiline": {
        "max": 1,
        "allowFirstLine": true
      }
    }]
  }
}
