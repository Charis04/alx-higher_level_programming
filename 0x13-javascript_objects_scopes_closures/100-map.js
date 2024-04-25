#!/usr/bin/node

const list = require('./100-data.js').list;

const newList = list.map((num, ind) => num * ind);
console.log(list);
console.log(newList);
