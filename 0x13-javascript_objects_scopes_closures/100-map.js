#!/usr/bin/node

const list = require('./100-data.js');

const new_list = list.map((num, ind) => num * ind);
console.log(list);
console.log(new_list);
