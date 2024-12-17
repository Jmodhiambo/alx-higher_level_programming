#!/usr/bin/node
const args = process.argv.slice(2);
const len = args.length;
let biggest = 0;
let secBiggest = 0;

for (let i = 0; i < len; i++) {
  args[i] = Number(args[i]);
}

if (len < 2) {
  console.log(0);
} else {
  for (let i = 0; i < len; i++) {
    if (args[i] > biggest) {
      secBiggest = biggest;
      biggest = args[i];
    } else if (args[i] > secBiggest) {
      secBiggest = args[i];
    }
  }
  console.log(secBiggest);
}
