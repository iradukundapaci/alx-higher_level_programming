#!/usr/bin/node
const counter = Math.floor(Number(process.argv[2]));
if (isNaN(counter)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < counter; i++) {
    console.log('C is fun');
  }
}
