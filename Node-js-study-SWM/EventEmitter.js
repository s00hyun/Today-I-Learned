var EventEmitter = require('events').EventEmitter;
var eventEmitter = new EventEmitter();

eventEmitter.on('customevent', function() {
	console.log('Event Occur!!');
});

eventEmitter.emit('customevent');