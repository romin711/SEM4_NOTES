const eventEmitter = require('events')
const ee = new eventEmitter()

ee.on('connection' , function() {
    console.log("connection done")
    ee.emit('data')
})

ee.on('data' , function() {
    console.log("data received")
})

ee.emit('connection')
console.log('thanks')