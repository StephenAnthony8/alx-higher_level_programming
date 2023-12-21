#!/usr/bin/node

exports.esrever = function (list) {
  const check = Array.isArray(list);
  const newList = [];

  if (check === true) {
    let x = list.length - 1;
    while (x > -1) {
      newList.push(list[x]);
      x--;
    }
  }
  return (newList);
};
