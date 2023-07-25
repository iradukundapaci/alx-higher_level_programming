#!/usr/bin/node
const length = Math.floor(Number(process.argv[2]));
if (isNaN(length)) {
  console.log('Missing size');
} else {
  for (let w = 0; w < length; w++) {
    console.log('X'.repeat(length));
  }
}
