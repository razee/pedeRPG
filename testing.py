import sfml as sf
import sys

RESOLUTION = 1024, 768
TITLE_TEXT = "testing"
window = sf.RenderWindow(sf.VideoMode(*RESOLUTION), TITLE_TEXT)
alreadyPressed = False
while window.is_open:
        eventList = window.poll_event()
        if eventList == sf.CloseEvent:
                window.close()
        elif type(eventList) == sf.KeyEvent:
                if eventList.pressed and not alreadyPressed:
                        alreadyPressed = True
                        print "pressed"
                if eventList.released:
                        alreadyPressed = False
                        print "released"
