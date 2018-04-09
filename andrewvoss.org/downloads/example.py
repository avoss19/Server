import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

RPL.servoWrite(0, 1000)
RRL.servoWrite(1, 2000)
