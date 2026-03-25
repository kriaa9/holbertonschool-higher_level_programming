#!/usr/bin/node
const argCount = process.argv.length - 2; // substract 2 to ignore 'node' and script name

if (argCount === 0) {
    console.log('No argument');
} else if (argCount === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
