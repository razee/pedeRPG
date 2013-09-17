import sfml as sf
import sys
import WorldCreator

#############################
# ## TESTING INPUT METHODS ##
#############################
# RESOLUTION = 1024, 768
# TITLE_TEXT = "testing"
# window = sf.RenderWindow(sf.VideoMode(*RESOLUTION), TITLE_TEXT)
# alreadyPressed = False
# while window.is_open:
#         eventList = window.poll_event()
#         if eventList == sf.CloseEvent:
#                 window.close()
#         elif type(eventList) == sf.KeyEvent:
#                 if eventList.pressed and not alreadyPressed:
#                         alreadyPressed = True
#                         print "pressed"
#                 if eventList.released:
#                         alreadyPressed = False
#                         print "released"

# #########################################
# ## TESTING RANDOM STAR DATA GENERATOR ##
# #########################################
# starmap = WorldCreator.StarMap()
# starmap.randomStarGenerator()

# ## Testing getData ##

# print starmap.getStarData('name','xyz10')

# ## Testing setData ##

# print "Old star data: ", starmap.getStarData('name','xyz11')
# starmap.setStarData('xyz11', (10,10,10), 10)
# print "New star data: ", starmap.getStarData('name','xyz11')