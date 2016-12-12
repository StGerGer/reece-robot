from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

from pyfirmata import Arduino, util

board = Arduino('/dev/ttyUSB0')     # If it doesn't work, try changing this number

# I believe these pins are for the RedBot, but I'm not sure. Check the pins

leftSpeedPin = 5
leftForwardPin = 8
leftBackwardPin = 7

rightSpeedPin = 6
rightForwardPin = 4
rightBackwardPin = 9

# Data: 0                    0                    0                    0                    000              000 (no spaces)
#       ^ R Motor Direction  ^ R Motor Direction  ^ L Motor Direction  ^ L Motor Direction  ^ R Motor Speed  ^ L Motor Speed
# Examples: 1001255255 Would be a turn, 1010255255 full speed forward, 1010100100 slower forward


class Echo(DatagramProtocol):

    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data, addr))
        # Write data to the pins
        board.digital[leftForwardPin].write(data[2])
        board.digital[leftBackwardPin].write(data[3])
        board.pwm[leftSpeedPin].write(data[4:6]/255 or 1) # In case there's no data or it's not correct

        board.digital[rightForwardPin].write(data[0])
        board.digital[rightBackwardPin].write(data[1])
        board.pwm[rightSpeedPin].write(data[7:9]/255 or 1) # In case there's no data or it's not correct
        # I forget what this does, but maybe it's important
        self.transport.write(data, addr)

reactor.listenUDP(9989, Echo()) # Defines port and class to run
reactor.run() # Starts server
