import sfml as sf
## GIC = GameInstanceClass, it tells us the name of parent class
class Player:
    def __init__(self, GIC):

        # Player default is a ball
        self.size = 10 # For ball shape size = radius = diameter/2
        self.shape = sf.CircleShape()
        self.shape.radius = self.size -3
        self.shape.outline_thickness = 3
        self.shape.outline_color = sf.Color.BLACK
        self.shape.fill_color = sf.Color.WHITE
        self.shape.origin = (self.shape.radius, self.shape.radius) # self.size is wrong: radius = size-3
        self.shape.position = (GIC.RESOLUTION[0]/2, GIC.RESOLUTION[1]/2)

    def movePlayer(self, GIC):
        step = 1
        stepfi = 1
        if GIC.controls['up']:
            self.shape.move((0,-step))


        elif GIC.controls['down']:
            self.shape.move((0,step))


        elif GIC.controls['left']:
            self.shape.move((-step,0))


        elif GIC.controls['right']:
            self.shape.move((step,0))


        elif GIC.controls['rotateL']:
            self.shape.rotate(-stepfi)


        elif GIC.controls['rotateR']:
            self.shape.rotate(stepfi)

class SpaceShip:
    def __init__(self, GIC, location = (0,0), AI = 0):
        self.vel = {'x':0, 'y':0} # Velocity of the ship in x in y direction
        self.dVEL = 1 # delta Velocity -> change of velocity in every step (if accelarating)
        self.angle = 0 # Angle of the ship

        pass

