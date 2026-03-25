#!/usr/bin/node

// Grab the first argument and attempt to convert it to an integer
const x = parseInt(process.argv[2], 10);

// Check if the conversion failed (meaning the user didn't pass a valid number)
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  // If it is a valid number, run the loop 'x' times.
  // Note: If x is a negative number (like -3), the condition (0 < -3) is false immediately,
  // so the loop just won't run, which matches the required output!
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
