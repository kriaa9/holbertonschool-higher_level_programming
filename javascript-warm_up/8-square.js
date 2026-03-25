#!/usr/bin/node

// Grab the argument and convert it to an integer
const size = parseInt(process.argv[2], 10);

// Check if the user failed to provide a valid number
if (isNaN(size)) {
  console.log('Missing size');
} else {
  // If size is a negative number, the loop condition (0 < -3) is false,
  // so nothing prints, matching the required output.
  for (let i = 0; i < size; i++) {
    // 'X'.repeat(size) creates a single string with 'size' number of X's.
    // console.log() automatically adds a new line after printing it.
    console.log('X'.repeat(size));
  }
}
