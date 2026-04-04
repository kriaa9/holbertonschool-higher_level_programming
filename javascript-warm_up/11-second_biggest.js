#!/usr/bin/env node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  // Sort descending and remove duplicates to ensure we find the second unique biggest
  const uniqueSorted = [...new Set(args)].sort((a, b) => b - a);

  if (uniqueSorted.length <= 1) {
    console.log(0);
  } else {
    console.log(uniqueSorted[1]);
  }
}
