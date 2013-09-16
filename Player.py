import sfml as sf

class Player:
    def __init__(self, GameInstanceClass):
        # Player default is a ball
        self.size = 10 # For ball shape size = radius = diameter/2
        self.shape = sf.CircleShape()
        self.shape.radius = self.size -3
        self.shape.outline_thickness = 3
        self.shape.outline_color = sf.Color.BLACK
        self.shape.fill_color = sf.Color.WHITE
        self.shape.origin = (self.shape.radius, self.shape.radius) # self.size is wrong: radius = size-3
        self.shape.position = (GameInstanceClass.RESOLUTION[0]/2, GameInstanceClass.RESOLUTION[1]/2)

    def movePlayer(self, GameInstanceClass):
        step = 1
        stepfi = 1
        if GameInstanceClass.controls['up']:
            self.shape.move((0,-step))


        elif GameInstanceClass.controls['down']:
            self.shape.move((0,step))


        elif GameInstanceClass.controls['left']:
            self.shape.move((-step,0))


        elif GameInstanceClass.controls['right']:
            self.shape.move((step,0))


        elif GameInstanceClass.controls['rotateL']:
            self.shape.rotate(-stepfi)


        elif GameInstanceClass.controls['rotateR']:
            self.shape.rotate(stepfi)

class SpaceShip:
    def __init__(self, GameInstanceClass, location = (0,0), AI = 0):
        self.vel = {'x':0, 'y':0} # Velocity of the ship in x in y direction
        self.dVEL = 1 # delta Velocity -> change of velocity in every step (if accelarating)
        self.angle = 0 # Angle of the ship

        pass

    