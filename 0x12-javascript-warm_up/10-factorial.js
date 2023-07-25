#!/usr/bin/node
function fact (n) {
  if (n === 1 || isNaN(n)) {
    return (1);
  }
  return n * fact(n - 1);
}

console.log(fact(Number(process.argv[2])));
