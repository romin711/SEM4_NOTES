const fs = require('fs');
// fs.mkdirSync('romin');
// console.log('Directory created successfully');

// fs.writeFileSync('romin/data2.txt', 'Namaste Duniya');
// console.log('File written successfully');

// fs.appendFileSync('romin/data2.txt', '\nNamaste Aliens');
// console.log('Data appended successfully');

// const data = fs.readFileSync('romin/data2.txt');
// console.log(data.toString());

// fs.renameSync('romin/data2.txt', 'romin/data3.txt');
// console.log('File renamed successfully');

fs.unlinkSync('romin/data3.txt');
console.log('File deleted successfully');