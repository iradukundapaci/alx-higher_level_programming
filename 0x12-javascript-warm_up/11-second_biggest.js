#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const li = process.argv.map(Number);
  li.slice(2, process.argv.length);
  li.sort((a, b) => a - b);
  console.log(li[li.length - 2]);
}
