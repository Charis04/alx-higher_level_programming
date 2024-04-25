#!/usr/bin/node

exports.converter = function (base) {
  return function convert (num, bas = base) {
    return parseInt(num, bas);
  };
};
