const fs = require('fs');   

fs.mkdir('myFolder', (err) => {
    if (err) throw err;
    console.log('Directory created successfully');
});

fs.mkdirSync('myFolder2');
console.log('Directory created successfully');