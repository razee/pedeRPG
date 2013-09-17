import sfml as sf
from random import randint

class StarMap:
    
    ## TODO
    #  We will call this class in game initialization
    #  __init__(self, GIC) --example--> GIC.StarMap.data()
    #  - create random starmap
    #       - fill matrix with star data --example--> StarMap.data()
    #           - location
    #               x,y,z
    #           - size
    #       - create a texture
    #           - size of a dot depends on 'z' and 'size'

    # StarMap.data = returns full matrix of star data
    # StarMap.getData('location', (x,y)) = returns data of star on location x,y of StarMap
    # StarMap.getData('name','STARTS NAME') = returns data of star with name 'STARS NAME'
    # 
    # StarMap.setData('name',[x,y,z,size])
    def __init__(self, settings = None):
        self.data = []
        print "StarMap __init__"
        if settings: # settings = [xMax, yMax, zMax, numStars, sizeMax]
            self.randomStarGenerator(settings[0],settings[1],settings[2],settings[3])
        else: self.randomStarGenerator()
        print "StarMap __init__ finished."

    def randomStarGenerator(self, xMax = 100, yMax = 100, zMax = 100, numStars = 100, sizeMax = 10):
        self.data.append(['Name','x','y','z','Size'])
        usedLocation = []
        print "Starting StarMap.randomGenerator(xMax="+str(xMax)+', yMax='+str(yMax)+', zMax='+str(zMax)+', numStars='+str(numStars)+', sizeMax='+str(sizeMax)+')'
        for i in range(numStars):
            name = 'xyz' + str(i)
            x = randint(1, xMax)
            y = randint(1, yMax)
            z = randint(1, zMax)
            size = randint(1, sizeMax)
            
            if [x,y,z] not in usedLocation:
                usedLocation.append([x,y,z])
                self.data.append([name,x,y,z,size])
        print "StarMap.data finished"

    def getStarData(self, keyName = None, key=None):
        if not keyName:
            return self.data
        elif keyName == 'name':
            for star in self.data:
                if star[0] == key:
                    return star