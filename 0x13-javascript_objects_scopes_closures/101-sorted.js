#!/usr/bin/node
const dict = require('./101-data').dict;
const newObj = {};

for (const key in dict) {
  const value = dict[key];
  if (!Object.hasOwn(newObj, value)) {
    newObj[value] = [];
  }
  newObj[value].push(key);
}
console.log(newObj);
