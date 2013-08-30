import sfml as sf
import sys
from PyQt4 import QtGui

class Menu(QtGui.QMainWindow):
    
    def __init__(self):
        super(Menu, self).__init__()

        self.initUI()

    
    def initUI(self):               
        new_game = QtGui.QAction('New Game', self)
        new_game.setShortcut('CTRL+N')
        new_game.setStatusTip('Start a new game')
        #new_game.triggered.connect(self.new)
        close_action = QtGui.QAction('Close', self)
        close_action.setShortcut("CTRL+Q")
        close_action.setStatusTip('Exit the game')
        #close_action.trigged.connect(self.close)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(new_game)
        file_menu.addAction(close_action)
        self.setGeometry(500, 500, 500, 500) 
        self.setWindowTitle('pedeRPG')
        self.show() 
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    



RESOLUTION = 1024, 768
WALLPAPER = 'faggot.png'
TITLE = "Placeholder for shitfuck"
window = sf.RenderWindow(sf.VideoMode(*RESOLUTION), TITLE)
texture = sf.Texture.from_file(WALLPAPER)
sprite = sf.Sprite(texture)
window.draw(sprite)
window.display()
sf.sleep(sf.seconds(5))