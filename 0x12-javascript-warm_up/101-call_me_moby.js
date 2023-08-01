#!/usr/bin/node

exports.callMeMoby = function (a, func) {
  for (let i = 0; i < a; i++) {
    func();
  }
};
