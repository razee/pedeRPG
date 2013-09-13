import sfml as sf
import sys

class Game:
    print "Game class created"
    def __init__(self):
        
        self.RESOLUTION = 1024, 768

        self.playerOne = Player(self)

        # BALL_RADIUS = 10
        # self.ball = sf.CircleShape()
        # self.ball.radius = BALL_RADIUS - 3
        # self.ball.outline_thickness = 3
        # self.ball.outline_color = sf.Color.BLACK
        # self.ball.fill_color = sf.Color.WHITE
        # self.ball.origin = (BALL_RADIUS / 2, BALL_RADIUS / 2)
        # self.ball.position = ((self.RESOLUTION[0]/2, self.RESOLUTION[1]/2))


        TITLE_TEXT = "pedeRPG"
        self.window = sf.RenderWindow(sf.VideoMode(*self.RESOLUTION), TITLE_TEXT)

        try:
            self.texture = sf.Texture.from_file('square.png')
            self.sprite = sf.Sprite(self.texture, sf.Rectangle((10, 10)))
        except IOError: exit(1)
        self.gameLoop()

    def gameLoop(self):
        while self.window.is_open:
            for event in self.window.events:
                print(event, type(event))
                if event == sf.CloseEvent:
                    self.window.close()
                elif sf.Keyboard.is_key_pressed(sf.Keyboard.W):
                    self.playerOne.movePlayer(0, -10) 
                elif sf.Keyboard.is_key_pressed(sf.Keyboard.S):
                    self.playerOne.movePlayer(0, 10)
                elif sf.Keyboard.is_key_pressed(sf.Keyboard.A):
                    self.playerOne.movePlayer(-10, 0)
                elif sf.Keyboard.is_key_pressed(sf.Keyboard.D):
                    self.playerOne.movePlayer(10, 0)
            self.window.clear(sf.Color.TRANSPARENT)
            self.window.draw(self.playerOne.shape)
            self.window.display()

class Player:

    def __init__(self, GameInstanceClass):
        # Player default is a ball
        self.size = 10 # For ball shape size = radius = diameter/2
        self.shape = sf.CircleShape()
        self.shape.radius = self.size -3
        self.shape.outline_thickness = 3
        self.shape.outline_color = sf.Color.BLACK
        self.shape.fill_color = sf.Color.WHITE
        self.shape.origin = (self.size / 2, self.size/2)
        self.shape.position = (GameInstanceClass.RESOLUTION[0]/2, GameInstanceClass.RESOLUTION[1]/2)

    def movePlayer(self,x,y):
        self.shape.move((x,y))


if __name__ == "__main__":
    myapp=Game()
