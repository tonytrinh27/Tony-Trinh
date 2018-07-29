import pyglet
from pyglet.window import mouse
import random
from pyglet.gl import *
from pyglet.window import mouse

window = pyglet.window.Window(800, 600, "Mario Error Version")
label = pyglet.text.Label(font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
image = pyglet.image.load('Dark_Cloud.png')
image_snake = pyglet.image.load('snake.png')
image_ground = pyglet.image.load('ground.png')
image_water = pyglet.image.load('2257a9e65d71596.jpg')
image_background = pyglet.image.load('beach-style-blue-background-1080p_qyvzckhb__F0000.png')
#Background
# batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
# foreground = pyglet.graphics.OrderedGroup(1)


#Edit Imageboom game code
background = pyglet.sprite.Sprite(image_background,
                                  group=background)
snake = pyglet.sprite.Sprite(image_snake, x=20, y=50)
snake1 = pyglet.sprite.Sprite(image_snake, x=700, y=50)
sprite = pyglet.sprite.Sprite(image, x=800, y=400)
sprite1 = pyglet.sprite.Sprite(image, x=1100, y=500)
sprite2 = pyglet.sprite.Sprite(image, x=1400, y=400)
ground = pyglet.sprite.Sprite(image_ground, x=0, y=-80)
ground1 = pyglet.sprite.Sprite(image_ground, x=400, y=-80)
ground2 = pyglet.sprite.Sprite(image_ground, x=1200, y=-80)
water = pyglet.sprite.Sprite(image_water, x=830, y=-220)
listgr = [ground,ground1,snake,water,snake1,ground2]
sprite.scale = 0.2
sprite1.scale = 0.2
sprite2.scale = 0.2
water.scale = 0.6
snake.scale = 0.2
snake1.scale = 0.2



@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print(x, y)
@window.event
def on_draw():
    window.clear()
    label.draw()
    background.draw()
    sprite.draw()
    sprite1.draw()
    sprite2.draw()
    snake.draw()
    snake1.draw()
    # ground.draw()boom game code
    # ground1.draw()
    # ground2.draw()
    # water.draw()
    for i in listgr:
        i.draw()
def ab(sprite):
    if sprite.x < -200:
        x = random.randint(750,900)
        y = random.randint(350,450)
        sprite.x = x
        sprite.y = y
    sprite.x -= 2

def gr():
    for i in listgr:
        if i.x < -430:
            i.x = window.width
        i.x -= 3
    # if ground.x < -400:
    #     ground.x = window.width
    # if ground1.x < -400:
    #     ground1.x = window.width
    # if ground2.x < -400:
    #     ground2.x = window.width
    # if water.x < -400:
    #     water.x = window.width
    # ground.x -= 1
    # ground1.x -= 1
    # ground2.x -= 1
    # water.x -= 1
def game_loop(_):
    ab(sprite)
    ab(sprite1)
    ab(sprite2)
    gr()
    # gr()
    # gr()
    # gr()
pyglet.clock.schedule(game_loop)
pyglet.app.run()


#, resizable=True
#window.set_minimum_size(800, 600)
