const eventEmitter = require('events')
const fs = require('fs')
const ee = new eventEmitter()

ee.on('write' , function() {
    fs.writeFile('b.txt' , 'hello ' , function(err) {
        if(err) throw err
        console.log('data written')

        ee.emit('append')
    })
})

ee.on('append' , function() {
    fs.appendFile('b.txt' , 'GM!' , function(err) {
        if(err) throw err
        console.log('appended')

        ee.emit('read')
    })
})

ee.on("read", function () { 
    fs.readFile("b.txt", "utf-8", function (err, data) { 
        if (err) throw err; 
        console.log("File Content:"); 
        console.log(data); 
    }); 
});

ee.emit('write')