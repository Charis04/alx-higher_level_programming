#!/usr/bin/node

function add (a, b) {
  return a + b;
}

// Access integers from command-line arguments (skip first two elements)
const firstInteger = parseInt(process.argv[2]);
const secondInteger = parseInt(process.argv[3]);

// Add the integers and print the result
const sum = add(firstInteger, secondInteger);
console.log(sum);
