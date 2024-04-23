#!/usr/bin/node

// Function to calculate factorial recursively
function factorial (num) {
  // Base case: Factorial of 0 and NaN is 1
  if (isNaN(num) || num === 0) {
    return 1;
  }

  // Recursive case: Factorial of n is n * factorial(n-1)
  return num * factorial(num - 1);
}

// Access integer from command-line argument (skip first two elements)
const number = parseInt(process.argv[2]);

// Calculate and print the factorial
const fact = factorial(number);
console.log(fact);
