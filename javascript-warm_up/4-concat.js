#!/usr/bin/node

// Grab the first custom argument at index 2
const arg1 = process.argv[2];

// Grab the second custom argument at index 3
const arg2 = process.argv[3];

// Use a template literal (the backticks ``) to easily insert the variables into a string.
// If arg1 or arg2 are missing, JavaScript will automatically print "undefined".
console.log(`${arg1} is ${arg2}`);
