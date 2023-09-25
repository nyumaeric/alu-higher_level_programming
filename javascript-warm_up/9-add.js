#!/usr/bin/node
const args = process.argv;
function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  if (a && b) {
    return (a + b);
  } else {
    return NaN;
  }
}
console.log(add((args[2]), args[3]));
