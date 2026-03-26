const fs = require('fs');
fs.rename('data2.txt', 'data3.txt', (err) => {
    if (err) throw err;
    console.log('File renamed successfully');
});



fs.renameSync('data3.txt', 'data4.txt');
console.log('File renamed successfully');