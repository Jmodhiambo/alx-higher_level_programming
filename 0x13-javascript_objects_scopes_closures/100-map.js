#!/usr/bin/node

const list = require('./100-data').list;
const newList = list.map(newElement);

console.log(list);
console.log(newList);

function newElement (element) {
  return element-- * element;
}
