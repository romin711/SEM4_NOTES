const EventEmitter = require('events');
const eventEmitter = new EventEmitter();

const radius = (radius) => {
    if (radius < 0) {
        console.log('radius must be +ve')
    }

    else {
        console.log('perimeter based on given radius is: ' + 2*Math.PI*radius)
    }
}

eventEmitter.on('radius' , radius)

eventEmitter.emit('radius', -5)
eventEmitter.emit('radius', 10)