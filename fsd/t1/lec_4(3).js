const fs = require('fs');
fs.appendFile('data2.txt', '\nHello World', (err) => {
    if (err) throw err;
    console.log('Data appended successfully');
});

fs.appendFileSync('data2.txt', '\nNamaste Aliens');
console.log('Data appended successfully');