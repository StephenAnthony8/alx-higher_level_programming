#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const check = Array.isArray(list);
  if (check === true) {
    for (let i = 0; i < list.length; i++) {
      /* let x = list[i]; */
      if (list[i] === searchElement) {
        count++;
      }
    }
  }
  return (count);
};
