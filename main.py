import sfml as sf
import sys
from EventListener import EventListener
from Player import Player
import WorldCreator
import Render


class Game:
    ### THIS IS GameInstanceClass, lets call it GIC
    print "Game Instance created."
    def __init__(self):
        print "Starting Game.__init__()."
        # Window init
        self.RESOLUTION = 1024, 768
        TITLE_TEXT = "pedeRPG"
        self.window = sf.RenderWindow(sf.VideoMode(*self.RESOLUTION), TITLE_TEXT)

        # Create control scheme
        self.controls = {'up':0, 'down':0, 'left':0, 'right':0, 'rotateL':0, 'rotateR':0}
        self.events = EventListener()

        # Create map class
        starMap = WorldCreator.StarMap()
        # Create star data
        starMap.randomStarGenerator()


        ## Create Player
        ## TODO
        # Player.SpaceShip(PARAMETERS)
        self.playerOne = Player(self)

        print "Game.__init__ finished. Starting gameLoop."
        # START OUR GAME LOOP!
        self.gameLoop()


    def gameLoop(self):
        # Game runs while the window is open
        while self.window.is_open:

            # We start every iteration with new inputs
            self.events.listen(self)

            # Calculate how these inputs change our world, player, etc.
            self.calculateIteration()

            # DRAW - RENDER EVERYTHING
            # clear screen
            self.window.clear(sf.Color.TRANSPARENT)

            self.window.draw(self.playerOne.shape)
            self.window.display()


    def calculateIteration(self):
        ## TODO
        # Calculate everything
        self.playerOne.movePlayer(self)



if __name__ == "__main__":
    myapp=Game()
