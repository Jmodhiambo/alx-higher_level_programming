#!/usr/bin/node
const args = process.argv.slice(2);

if (!args[0]) {
  console.log('Missing number of occurrences');
}
const number = Number(args[0]);

for (let i = 0; i < number; i++) {
  console.log('C is fun');
}
