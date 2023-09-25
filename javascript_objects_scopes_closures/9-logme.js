#!/usr/bin/node
let Arguments = -1;
exports.logMe = function (item) {
  Arguments++;
  console.log(Arguments + ': ' + item);
};
