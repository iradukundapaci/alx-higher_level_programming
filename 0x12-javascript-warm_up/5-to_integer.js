#!/usr/bin/node
const myNumber = Math.floor(Number(process.argv[2]));
if (isNaN(myNumber)) {
  console.log('Not a number');
} else {
  console.log('My number:', myNumber);
}
