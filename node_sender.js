// Note: In order for this to work properly, the xevEmitter is linux-only.
// There may be a way for this to work on Windows (since 10 now has bash), but I haven't tested it.

const dgram = require('dgram');

const xevEmitter = require('xev-emitter')(process.stdin)

const client = dgram.createSocket('udp4'); // Creates a UDP socket for sending packets
const port = 9989; // Port that the robot's RPi is listening on
const host = '10.80.49.162'; // IP of the RPi

var messageString;
var message;

xevEmitter.on('KeyPress', function(key) { // Runs on keypress
    if(key == 'w') {
        messageString = '1010255255';   // 1010 = forward, 255255 = full speed
    } else if (key == 's') {
        messageString = '0101255255';   // 0101 = backward
    } else if (key == 'a') {
        messageString = '1001255255';   // 1001 = left
    } else if (key == 'd') {
        messageString = '0110255255';   // 0110 = right
    } else if (key == 'space') {
        messageString = '0000255255';   // 0000 = stop
    }

    message = new Buffer(messageString); // Make the message part of the packet
    client.send(message, 0, message.length, port, host, function (err, bytes) {}); // Send packet
});

xevEmitter.on('KeyRelease', function(key) { // When the key is no longer being pressed
    messageString = '0000255255';           // Make it stop
    message = new Buffer(messageString);
    client.send(message, 0, message.length, port, host, function (err, bytes) {});
});
