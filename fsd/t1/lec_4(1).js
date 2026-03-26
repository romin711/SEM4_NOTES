// using toString()
const fs = require('fs');

// fs.readFile('data.txt', (err, data) => {
//     if (err) throw err;
//     // console.log(data.toString());
//     console.log(data);
//     }
// )



fs.readFile('data.txt', 'utf-8' ,(err, data) => {
    if (err) throw err;
    // console.log(data.toString());
    console.log(data);
    }
)




// const data = fs.readFileSync('data.txt');
// console.log(data.toString());