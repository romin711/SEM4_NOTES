const fs = require('fs');

fs.rmdir('myFolder2', (err) => {
    if (err) throw err;
    console.log('Directory deleted successfully');
});

fs.rmdirSync('myFolder');
console.log('Directory deleted successfully');