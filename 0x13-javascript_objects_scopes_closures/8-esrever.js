#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    // console.log(list[i]);
    newlist.push(list[i]);
  }
  return newlist;
};
