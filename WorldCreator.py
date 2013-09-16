import sfml as sf

class StarMap:
    pass
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

    # StarMap.data() = returns full matrix of star data
    # StarMap.data('location',x,y) = returns data of star on location x,y of StarMap
    # StarMap.data('name','STARTS NAME') = returns data of star with name 'STARS NAME'
    # 
    # StarMap.setData('name',[x,y,z,size])