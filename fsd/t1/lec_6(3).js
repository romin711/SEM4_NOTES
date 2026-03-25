// removing listener

const EventEmitter = require('events')
const eventEmitter = new EventEmitter()

var fun1 = (msg) => {
    console.log('message from fun1: ' + msg)
    // console.log('a')
}

var fun2 = (msg) => {
    console.log('message form fun2: ' + msg)
    // console.log('b')
}

eventEmitter.on('myEvent1' , fun1)
eventEmitter.on('myEvent2' , fun2)
eventEmitter.on('myEvent1' , fun1)
eventEmitter.on('myEvent2' , fun2)

// eventEmitter.removeListener('myEvent2' , fun2)
// eventEmitter.removeAllListeners('myEvent2')

eventEmitter.emit('myEvent2' , 'lju')
eventEmitter.emit('myEvent1' , 'xyz')

console.log('myEvent1' , eventEmitter.listenerCount('myEvent1'))
console.log('myEvent2' , eventEmitter.listenerCount('myEvent2'))