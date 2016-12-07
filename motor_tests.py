from pyfirmata import Arduino, util, time

port = "/dev/ttyUSB1"
board = Arduino(port)

it = util.Iterator(board)
it.start()

lPWM = board.get_pin('d:6:p')
rPWM = board.get_pin('d:5:p')

board.digital[2].write(0)   # Left probably
board.digital[4].write(1)

board.digital[7].write(0)   # Right probably
board.digital[8].write(1)

board.analog[4].enable_reporting()

print(board.analog[4].read)

board.exit()
