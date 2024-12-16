#!/usr/bin/node
const args = process.argv.slice(1);

if (args[2]) {
  console.log('Arguments found');
} else if (args[1]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
