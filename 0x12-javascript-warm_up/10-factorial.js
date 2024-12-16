#!/usr/bin/node
const args = process.argv.slice(2);
let factorial = 1;
const count = Number(args[0]) || 1; /* If NaN 1 is assigned instead. */

for (let i = 1; i <= count; i++) {
  factorial = factorial * i;
}
console.log(factorial);
