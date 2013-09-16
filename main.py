import sfml as sf
import sys
import Player
import WorldCreator

class Game:
    print "Game class created"
    def __init__(self):
        # Window init
        self.RESOLUTION = 1024, 768
        TITLE_TEXT = "pedeRPG"
        self.window = sf.RenderWindow(sf.VideoMode(*self.RESOLUTION), TITLE_TEXT)

        # Create control scheme
        self.controls = {'up':0, 'down':0, 'left':0, 'right':0, 'rotateL':0, 'rotateR':0}
        self.events = EventListener()

        # Create map
        # starMap = WorldCreator.StarMap(PARAMETERS) # TODO WorldCreator.StarMap

        ## Create Player
        ## TODO
        # Player.SpaceShip(PARAMETERS)
        self.playerOne = Player.Player(self)

        # START OUR GAME LOOP!
        self.gameLoop()

    def gameLoop(self):
        # Game runs while the window is open
        while self.window.is_open:
            # We start every iteration with new inputs
            self.events.listen(self)
            # Calculate how these inputs change our world, player, etc.
            self.calculateIteration()

            # CLEAR SCREEN
            self.window.clear(sf.Color.TRANSPARENT)
            # DRAW - RENDER EVERYTHING
            self.window.draw(self.playerOne.shape)
            self.window.display()


    def calculateIteration(self):
        self.playerOne.movePlayer(self)
        ## TODO
        # Update everything

class EventListener:
    def __init__(self):
        
        self.eventList = sf.Event()
               
    def listen(self, gameInstanceClass):
        self.eventList = gameInstanceClass.window.poll_event()
        if self.eventList == sf.CloseEvent:
            gameInstanceClass.window.close()
        elif type(self.eventList) is sf.KeyEvent and self.eventList.pressed:

            if not gameInstanceClass.controls['up'] and self.eventList.code is sf.Keyboard.W:
                gameInstanceClass.controls['up'] = 1

            elif not gameInstanceClass.controls['down'] and self.eventList.code is sf.Keyboard.S:
                gameInstanceClass.controls['down'] = 1

            elif not gameInstanceClass.controls['left'] and self.eventList.code is sf.Keyboard.A:
                gameInstanceClass.controls['left'] = 1

            elif not gameInstanceClass.controls['right'] and self.eventList.code is sf.Keyboard.D:
                gameInstanceClass.controls['right'] = 1

            elif not gameInstanceClass.controls['rotateL'] and self.eventList.code is sf.Keyboard.Q:
                gameInstanceClass.controls['rotateL'] = 1

            elif not gameInstanceClass.controls['rotateR'] and self.eventList.code is sf.Keyboard.E:
                gameInstanceClass.controls['rotateR'] = 1


        elif type(self.eventList) is sf.KeyEvent and self.eventList.released:
            if self.eventList.code is sf.Keyboard.W:
                gameInstanceClass.controls['up'] = 0

            elif self.eventList.code is sf.Keyboard.S:
                gameInstanceClass.controls['down'] = 0

            elif self.eventList.code is sf.Keyboard.A:
                gameInstanceClass.controls['left'] = 0

            elif self.eventList.code is sf.Keyboard.D:
                gameInstanceClass.controls['right'] = 0

            elif self.eventList.code is sf.Keyboard.Q:
                gameInstanceClass.controls['rotateL'] = 0

            elif self.eventList.code is sf.Keyboard.E:
                gameInstanceClass.controls['rotateR'] = 0




        # self.event = gameInstanceClass.window.poll_event()
        # print(self.event, type(self.event)) # For Dev purposes

        # if self.event == sf.CloseEvent:
        #     gameInstanceClass.window.close()
        # elif sf.Keyboard.is_key_pressed(sf.Keyboard.W):
        #     gameInstanceClass.controls['up'] = 1
        # elif sf.Keyboard.is_key_pressed(sf.Keyboard.S):
        #     gameInstanceClass.controls['down'] = 1
        # elif sf.Keyboard.is_key_pressed(sf.Keyboard.A):
        #     gameInstanceClass.controls['left'] = 1
        # elif sf.Keyboard.is_key_pressed(sf.Keyboard.D):
        #     gameInstanceClass.controls['right'] = 1
        # elif sf.Keyboard.is_key_pressed(sf.Keyboard.Q):
        #     gameInstanceClass.controls['rotateL'] = 1
        # elif sf.Keyboard.is_key_pressed(sf.Keyboard.E):
        #     gameInstanceClass.controls['rotateR'] = 1


if __name__ == "__main__":
    myapp=Game()
