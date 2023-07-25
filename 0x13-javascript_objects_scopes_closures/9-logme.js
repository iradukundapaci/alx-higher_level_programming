#!/usr/bin/node
exports.logMe = (function (item) {
  let counter = 0;
  return (item) => {
    console.log(counter + ': ' + item);
    counter++;
  };
})();
