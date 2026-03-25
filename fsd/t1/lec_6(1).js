// // event module

// const eventEmitter = require('events')
// const ee = new eventEmitter()
// ee.on('start' , () => {
//     console.log('started')
// })
// ee.emit('start')



const eventEmitter = require('events')
const ee = new eventEmitter()

ee.on('start' , (start, end) => {
    console.log(`started from ${start} to ${end}`)
})

ee.emit('start' , 1 , 50)