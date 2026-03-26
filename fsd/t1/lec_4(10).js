var fs = require('fs')
fs.writeFileSync('s1.txt', '20 -12 90 87 34 67');

data = fs.readFileSync('s1.txt' , 'utf-8')
data = data.split(' ')
d = data.sort((a, b) => a - b)
// console.log(d);


var a = fs.readFileSync('s1.txt');
console.log((a[1]));