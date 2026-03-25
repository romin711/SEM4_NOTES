const EventEmitter = require('events');
const eventEmitter = new EventEmitter();

const listener1 = (msg) => {
    console.log('Listener 1 received: ' + msg);
};

const listener2 = (msg) => {
    console.log('Listener 2 received: ' + msg);
};

eventEmitter.on('commonEvent', listener1);
eventEmitter.on('commonEvent', listener2);

eventEmitter.emit('commonEvent', 'hello world');
console.log('number of commonEvent:', eventEmitter.listenerCount('commonEvent'));

eventEmitter.removeListener('commonEvent' , listener2 )

eventEmitter.emit('commonEvent', 'namaste duniya');
console.log('number of listeners after removing: ' + eventEmitter.listenerCount('commonEvent'))