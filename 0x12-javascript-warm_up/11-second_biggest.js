#!/usr/bin/node

function secondBiggest (val) {
  let rtnVal = 0;
  if (val.length > 3) {
    let biggestArr;
    const newArr = (val.slice(2)).map(function (str) {
      return parseInt(str);
    });
    /* newArr =  */newArr.sort();
    biggestArr = rtnVal = newArr[0];

    for (let i = 0; i < newArr.length; i++) {
      if (biggestArr < newArr[i]) {
        rtnVal = biggestArr;
        biggestArr = newArr[i];
      }
    }
  }
  return (rtnVal);
}

console.log(secondBiggest(process.argv));
