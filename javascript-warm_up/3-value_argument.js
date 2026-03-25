#!/usr/bin/node

// Grab the value sitting at index 2 of the process.argv array.
// Index 0 is the Node executable, Index 1 is the file path.
// Index 2 is where the first user-provided argument will be.
const firstArg = process.argv[2];

// Check if that specific "seat" in the array is empty.
// If the user didn't type an argument, JavaScript evaluates it as undefined.
if (firstArg === undefined) {
  console.log('No argument');
} else {
  // If it is NOT undefined, it means an argument is there, so we print it.
  console.log(firstArg);
}
