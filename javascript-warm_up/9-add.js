#!/usr/bin/node

// Define the function as required by the prompt
function add(a, b) {
  return a + b;
}

// Grab the first and second arguments and parse them as base-10 integers
const num1 = parseInt(process.argv[2], 10);
const num2 = parseInt(process.argv[3], 10);

// Call the function and print the result
console.log(add(num1, num2));
