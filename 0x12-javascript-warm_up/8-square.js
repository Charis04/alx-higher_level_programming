#!/usr/bin/node

const x = parseInt(process.argv[2]);
let str = 'X';
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 1; i < x; i++) {
    str += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(str);
  }
}
