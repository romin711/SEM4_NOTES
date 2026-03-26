const fs = require('fs');

// fs.writeFile('data2.txt', 'Hello World', (err) => {
    // if (err) throw err;
    // console.log('File written successfully');
    // }
// )


fs.writeFileSync('data2.txt', 'Namaste Duniya');
console.log('File written successfully');