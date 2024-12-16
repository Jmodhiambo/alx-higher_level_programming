#!/usr/bin/node
const args = process.argv.slice(2);

const number = Number(args[0]);
if (number) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
