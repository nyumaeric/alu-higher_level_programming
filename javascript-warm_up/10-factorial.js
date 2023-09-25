#!/usr/bin/node
const args = process.argv;
function factorial (a) {
  a = parseInt(a);
  if (a && a > 1) {
    return (a * factorial(a - 1));
  } else if (isNaN(a) || a === 1 || a === 0) {
    return (1);
  } else {
    return NaN;
  }
}
console.log(factorial(args[2]));
