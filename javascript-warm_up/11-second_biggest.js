#!/usr/bin/node
const ary = process.argv;
ary.shift();
ary.shift();
if (ary[1]) {
  ary.sort(function (a, b) { return b - a; });
  console.log(ary[1]);
} else {
  console.log(0);
}
