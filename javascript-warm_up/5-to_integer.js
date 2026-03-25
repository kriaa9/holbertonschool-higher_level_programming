#!/usr/bin/node

// Grab the first argument
const firstArg = process.argv[2];

// Try to convert it to an integer using base 10
const num = parseInt(firstArg, 10);

// Check if the conversion failed (resulting in Not-a-Number)
if (isNaN(num)) {
  console.log('Not a number');
} else {
  // If it succeeded, print the integer
  console.log(`My number: ${num}`);
}
