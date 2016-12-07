const dgram = require('dgram');

const xevEmitter = require('xev-emitter')(process.stdin)

const client = dgram.createSocket('udp4');
const port = 9989;
const host = '10.80.49.162';

var messageString;
var message;

xevEmitter.on('KeyPress', function(key) {
    console.log(key+" was pressed");
    if(key == 'w') {
        messageString = '1010255255';
    } else if (key == 's') {
        messageString = '0101255255';
    } else if (key == 'a') {
        messageString = '1001255255';
    } else if (key == 'd') {
        messageString = '0110255255';
    } else if (key == 'space') {
        console.log('stop');
        messageString = '0000255255';
    }

    message = new Buffer(messageString);
    client.send(message, 0, message.length, port, host, function (err, bytes) {});
});

xevEmitter.on('KeyRelease', function(key) {
    messageString = '0000255255';
    message = new Buffer(messageString);
    client.send(message, 0, message.length, port, host, function (err, bytes) {});
});
