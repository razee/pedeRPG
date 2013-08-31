import sfml as sf
import sys

ball_radius = 10

RESOLUTION = 1024, 768
ball = sf.CircleShape()
ball.radius = ball_radius - 3
ball.outline_thickness = 3
ball.outline_color = sf.Color.BLACK
ball.fill_color = sf.Color.WHITE
ball.origin = (ball_radius / 2, ball_radius / 2)
ball.position = ((RESOLUTION[0]/2, RESOLUTION[1]/2))


title_text = "pedeRPG"
window = sf.RenderWindow(sf.VideoMode(*RESOLUTION), title_text)

try:
    texture = sf.Texture.from_file('square.png')
    sprite = sf.Sprite(texture, sf.Rectangle((10, 10)))
except IOError: exit(1)

while window.is_open:
    for event in window.events:
        print(event, type(event))
        if event == sf.CloseEvent:
            window.close()
        elif sf.Keyboard.is_key_pressed(sf.Keyboard.W):
            ball.move((0, -10)) 
        elif sf.Keyboard.is_key_pressed(sf.Keyboard.S):
            ball.move((0, 10))
        elif sf.Keyboard.is_key_pressed(sf.Keyboard.A):
            ball.move((-10, 0))
        elif sf.Keyboard.is_key_pressed(sf.Keyboard.D):
            ball.move((10, 0))
    window.clear(sf.Color.TRANSPARENT)
    window.draw(ball)
    window.display()
