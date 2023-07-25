#!/usr/bin/node
exports.esrever = function (list) {
  const revs = [];
  for (const i of list) {
    revs.unshift(i);
  }
  return revs;
};
