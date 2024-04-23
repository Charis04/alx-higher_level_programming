#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);
if (typeof firstArg === "number" && !isNaN(firstArg)) {
  console.log('My number:', firstArg);
} else {
  console.log('Not a number');
}
