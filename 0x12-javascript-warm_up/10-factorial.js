#!/usr/bin/node
const args = process.argv.slice(2);
const count = Number(args[0]);

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(count));
