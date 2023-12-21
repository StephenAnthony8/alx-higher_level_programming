#!/usr/bin/node

if ((process.argv).length > 2) {
  const myArgs = (process.argv).length;
  console.log(myArgs === 3 ? 'Argument found' : 'Arguments found');
} else {
  console.log('No argument');
}
