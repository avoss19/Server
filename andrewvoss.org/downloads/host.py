# --------------------------------File on Robot---------------------------------
# Hosts a TCP connection and interprets the data recieved
import sys, os, socket
import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

######################
##    Host Info     ##
######################
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
host = sys.argv[1]
server_address = (host, 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

######################
##      Main        ##
######################
while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(9)
            data = data.split(' ')

            RPL.servoWrite(0, int(data[0]))
            RPL.servoWrite(1, int(data[1]))

    finally:
        connection.close()
