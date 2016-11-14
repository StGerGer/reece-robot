from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

# Data: 0                    0                    0                    0                    000              000 (no spaces)
#       ^ R Motor Direction  ^ R Motor Direction  ^ L Motor Direction  ^ L Motor Direction  ^ R Motor Speed  ^ L Motor Speed
# Examples: 1001255255 Would be a full right (maybe left) turn, 1010255255 full speed forward, 1010100100 slower forward


class Echo(DatagramProtocol):

    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data, addr))
        self.transport.write(data, addr)

reactor.listenUDP(9999, Echo())
reactor.run()
