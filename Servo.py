from pyfirmata import Arduino,SERVO
import time

class servo():
    def __init__(self,pin,board):
        board = Arduino(board)
        self.board = board
        self.pin = pin
        board.digital[pin].mode = SERVO

        

    def move(self,angle):
        self.board.digital[self.pin].write(angle)
        time.sleep(0.00015)

