import sfml as sf
import sys

class Game:
    print "Game class created"
    def __init__(self):
        
        self.RESOLUTION = 1024, 768

        BALL_RADIUS = 10
        self.ball = sf.CircleShape()
        self.ball.radius = BALL_RADIUS - 3
        self.ball.outline_thickness = 3
        self.ball.outline_color = sf.Color.BLACK
        self.ball.fill_color = sf.Color.WHITE
        self.ball.origin = (BALL_RADIUS / 2, BALL_RADIUS / 2)
        self.ball.position = ((self.RESOLUTION[0]/2, self.RESOLUTION[1]/2))


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
                    self.ball.move((0, -10)) 
                elif sf.Keyboard.is_key_pressed(sf.Keyboard.S):
                    self.ball.move((0, 10))
                elif sf.Keyboard.is_key_pressed(sf.Keyboard.A):
                    self.ball.move((-10, 0))
                elif sf.Keyboard.is_key_pressed(sf.Keyboard.D):
                    self.ball.move((10, 0))
            self.window.clear(sf.Color.TRANSPARENT)
            self.window.draw(self.ball)
            self.window.display()

if __name__ == "__main__":
    myapp=Game()
