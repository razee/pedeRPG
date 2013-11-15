import sfml as sf
from random import randint

class StarMap:
    #  We will call this class in game initialization
    #
    ## DONE ##  - create random starmap
    ## DONE ##       - fill matrix with star data --example--> StarMap.data()
    ## DONE ##           - location
    ## DONE ##               x,y,z
    ## DONE ##           - size
    ##
    ## DONE ## StarMap.data = returns full matrix of star data
    ## DONE ## StarMap.getStarData('location', (x,y,z)) = returns data of star on location x,y of StarMap 
    ## DONE ## StarMap.getStarData('name','STARTS NAME') = returns data of star with name 'STARS NAME'
    ## DONE ## StarMap.setStarData('name',location,size])

    ## TODO ##
    #       - create a texture
    #           - size of a dot depends on 'z' and 'size'

    def __init__(self, settings = None):
        self.data = []
        print "StarMap __init__"
        if settings: # settings = [xMax, yMax, zMax, numStars, sizeMax]
            self.randomStarGenerator(settings[0],settings[1],settings[2],settings[3])
        else: self.randomStarGenerator()
        print "StarMap __init__ finished."

    def randomStarGenerator(self, xMax = 100, yMax = 100, zMax = 100, numStars = 100, sizeMax = 10):
        self.data.append(['Name','Location','Size'])
        usedLocation = []
        print "Starting StarMap.randomGenerator(xMax="+str(xMax)+', yMax='+str(yMax)+', zMax='+str(zMax)+', numStars='+str(numStars)+', sizeMax='+str(sizeMax)+')'
        for i in range(numStars):
            name = 'xyz' + str(i)
            location = (randint(1, xMax), randint(1, yMax), randint(1, zMax))
            # x = randint(1, xMax)
            # y = randint(1, yMax)
            # z = randint(1, zMax)
            size = randint(1, sizeMax)
            
            if location not in usedLocation:
                usedLocation.append(location)
                self.data.append([name,location,size])
        print "StarMap.data finished"

    def getStarData(self, keyName = None, key=None):
        if not keyName:
            return self.data
        elif keyName == 'name':
            index = 0
            for star in self.data:
                if star[0] == key:
                    return star, index
                index += 1
        elif keyName == 'location':
            for star in self.data:
                if key in star:
                    return star

    def setStarData(self, name, location, size, new=False):
        if new:
            self.data.append([name, location, size])
        else:
            oldData, index = self.getStarData('name', name)
            self.data[index][1:] = location, size