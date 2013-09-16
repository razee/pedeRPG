import sfml as sf
import sys
import Player

class Game:
    print "Game class created"
    def __init__(self):
        # Window init
        self.RESOLUTION = 1024, 768
        TITLE_TEXT = "pedeRPG"
        self.window = sf.RenderWindow(sf.VideoMode(*self.RESOLUTION), TITLE_TEXT)
        # Create control scheme
        self.controls = {'up':0, 'down':0, 'left':0, 'right':0, 'rotateL':0, 'rotateR':0}
        self.events = EventListener(self)
        # Create map
        # map = StarMap(self) # TODO StarMap

        # Create Player
        self.playerOne = Player.Player(self)

        try:
            self.texture = sf.Texture.from_file('square.png')
            self.sprite = sf.Sprite(self.texture, sf.Rectangle((10, 10)))
        except IOError: exit(1)
        self.gameLoop()

    def gameLoop(self):
        while self.window.is_open:
            self.events.listen(self)
            self.playerOne.movePlayer(self)
            # for event in self.window.events:
            #     print(event, type(event))
            #     if event == sf.CloseEvent:
            #         self.window.close()
            #     elif sf.Keyboard.is_key_pressed(sf.Keyboard.W):
            #         self.playerOne.movePlayer(0, -10) 
            #     elif sf.Keyboard.is_key_pressed(sf.Keyboard.S):
            #         self.playerOne.movePlayer(0, 10)
            #     elif sf.Keyboard.is_key_pressed(sf.Keyboard.A):
            #         self.playerOne.movePlayer(-10, 0)
            #     elif sf.Keyboard.is_key_pressed(sf.Keyboard.D):
            #         self.playerOne.movePlayer(10, 0)
            #     elif sf.Keyboard.is_key_pressed(sf.Keyboard.Q):
            #         self.playerOne.rotatePlayer(-10)
            #     elif sf.Keyboard.is_key_pressed(sf.Keyboard.E):
            #         self.playerOne.rotatePlayer(10)
            self.window.clear(sf.Color.TRANSPARENT)
            self.window.draw(self.playerOne.shape)
            self.window.display()
            print self.controls


    def calculateIteration(self):
        self.playerOne.movePlayer()

# class Player:
#     def __init__(self, GameInstanceClass):
#         # Player default is a ball
#         self.size = 10 # For ball shape size = radius = diameter/2
#         self.shape = sf.CircleShape()
#         self.shape.radius = self.size -3
#         self.shape.outline_thickness = 3
#         self.shape.outline_color = sf.Color.BLACK
#         self.shape.fill_color = sf.Color.WHITE
#         self.shape.origin = (self.shape.radius, self.shape.radius) # self.size is wrong: radius = size-3
#         self.shape.position = (GameInstanceClass.RESOLUTION[0]/2, GameInstanceClass.RESOLUTION[1]/2)

#     def movePlayer(self, GameInstanceClass):
#         step = 1
#         stepfi = 1
#         if GameInstanceClass.controls['up']:
#             self.shape.move((0,-step))


#         elif GameInstanceClass.controls['down']:
#             self.shape.move((0,step))


#         elif GameInstanceClass.controls['left']:
#             self.shape.move((-step,0))


#         elif GameInstanceClass.controls['right']:
#             self.shape.move((step,0))


#         elif GameInstanceClass.controls['rotateL']:
#             self.shape.rotate(-stepfi)


#         elif GameInstanceClass.controls['rotateR']:
#             self.shape.rotate(stepfi)


class EventListener:
    def __init__(self, gameInstanceClass):
        
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



class ViewZone:

    def __init__(self, parentWindow, locationX = 0, locationY = 0):
        ## TODO
        # Add:
        # 
        pass

class StarMap:
    pass
    ## TODO
    #  We will call this class in game initialization
    #  __init__(self, GameInstanceClass) --example--> GameInstanceClass.StarMap.data()
    #  - create random starmap
    #       - fill matrix with star data --example--> StarMap.data()
    #           - location
    #               x,y,z
    #           - size
    #       - create a texture
    #           - size of a dot depends on 'z' and 'size'

    # StarMap.data() = returns full matrix of star data
    # StarMap.data('location',x,y) = returns data of star on location x,y of StarMap
    # StarMap.data('name','STARTS NAME') = returns data of star with name 'STARS NAME'
    # 
    # StarMap.setData('name',[x,y,z,size])

if __name__ == "__main__":
    myapp=Game()
