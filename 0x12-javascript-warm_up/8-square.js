#!/usr/bin/node
let toprint = '';
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    for (let y = 0; y < process.argv[2]; y++) {
      toprint += 'X';
    }
    console.log(toprint);
    toprint = '';
  }
}
