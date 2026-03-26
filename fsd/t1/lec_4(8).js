const fs = require('fs');

fs.copyFile('data4.txt', 'data5.txt', (err) => {
    if (err) throw err;
    console.log('File copied successfully');
});

fs.copyFileSync('data4.txt', 'data6.txt');
console.log('File copied successfully');