class Player:
    def moveRight(self):
        pass
    def moveleft(self):
        pass
    def moveTop(self):
        pass

class Remote:
    pass

remote1 = Remote()
player1 = Player()

if remote1.rightPressed():
    player1.moveRight()
