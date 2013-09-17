import sfml as sf

class EventListener:
    def __init__(self):
        
        self.eventList = sf.Event()
               
    def listen(self, GIC):
        self.eventList = GIC.window.poll_event()
        if self.eventList == sf.CloseEvent:
            print "Closing."
            GIC.window.close()
        elif type(self.eventList) is sf.KeyEvent and self.eventList.pressed:

            if not GIC.controls['up'] and self.eventList.code is sf.Keyboard.W:
                GIC.controls['up'] = 1

            elif not GIC.controls['down'] and self.eventList.code is sf.Keyboard.S:
                GIC.controls['down'] = 1

            elif not GIC.controls['left'] and self.eventList.code is sf.Keyboard.A:
                GIC.controls['left'] = 1

            elif not GIC.controls['right'] and self.eventList.code is sf.Keyboard.D:
                GIC.controls['right'] = 1

            elif not GIC.controls['rotateL'] and self.eventList.code is sf.Keyboard.Q:
                GIC.controls['rotateL'] = 1

            elif not GIC.controls['rotateR'] and self.eventList.code is sf.Keyboard.E:
                GIC.controls['rotateR'] = 1


        elif type(self.eventList) is sf.KeyEvent and self.eventList.released:
            if self.eventList.code is sf.Keyboard.W:
                GIC.controls['up'] = 0

            elif self.eventList.code is sf.Keyboard.S:
                GIC.controls['down'] = 0

            elif self.eventList.code is sf.Keyboard.A:
                GIC.controls['left'] = 0

            elif self.eventList.code is sf.Keyboard.D:
                GIC.controls['right'] = 0

            elif self.eventList.code is sf.Keyboard.Q:
                GIC.controls['rotateL'] = 0

            elif self.eventList.code is sf.Keyboard.E:
                GIC.controls['rotateR'] = 0