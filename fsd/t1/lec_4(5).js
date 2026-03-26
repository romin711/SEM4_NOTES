const fs = require('fs');

fs.unlink('data10.txt' , (err) => {    
    if (err) throw err;
    console.log('File deleted successfully');
});

fs.unlinkSync('data11.txt');
console.log('File deleted successfully');