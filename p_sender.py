from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

import curses

robotIP = 'localhost'

class Sender(DatagramProtocol):   # Basic format: http://stackoverflow.com/questions/3632210/udp-client-and-server-with-twisted-python
    def __init__(self, packet, host=robotIP, port=9999):
        self.packet = packet.pack()
        self.host = host
        self.port = port

    def startProtocol(self):
        self.transport.write(self.packet, (self.host, self.port))

if __name__ == "__main__":
    packet = Packet()
    packet.packet_type = 1
    packet.payload = '1010255255'

    s = Sender(packet)

    reactor.listenMulticast(9999, MyProtocol(), listenMultiple=True)
    reactor.listenMulticast(9999, s, listenMultiple=True)
    reactor.callLater(4, reactor.stop)
    reactor.run()
