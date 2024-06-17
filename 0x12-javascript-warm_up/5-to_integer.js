#!/usr/bin/node
console.log(!isNaN(process.argv[2]) ? `My number: ${process.argv[2]}` : 'Not a number');
