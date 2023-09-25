#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  list.forEach(function (element) {
    newList.unshift(element);
  });
  return newList;
};
