const fs = require("fs")

if(!fs.existsSync('myFolder1')) {
    fs.mkdir('myFolder1' , (err) => {
        if(err) throw err;
        console.log('folder created');
    })
}

else {
    console.log('folder already exists');
}