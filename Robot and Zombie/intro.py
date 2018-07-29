import pyglet
from pyglet.window import mouse
import random


label = pyglet.text.Label(font_size=36, x = 200, y = 520, color = (0, 255 ,255 ,255))
label1 = pyglet.text.Label(font_size=20, x = 250, y = 470, color = (255, 0 ,0 ,255))
nameteam = pyglet.text.Label(font_size=15, x = 380, y = 210, color = (255, 255 ,0 ,255))
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
label.text = "Robot VS Zombie"
label1.text = "Press Space To Start"
nameteam.text = "NP Team"
# background INTRO
image_intro_bg = pyglet.image.load('img/map/BG.png')
intro_BG = pyglet.sprite.Sprite(image_intro_bg, group = background)
intro_BG.scale = 0.9

image_zombie_intro = pyglet.image.load('img/zombie/zombie11.png')
intro_zombie = pyglet.sprite.Sprite(image_zombie_intro, x = 450, y = 30)
intro_zombie.scale = 0.9

image_robot_intro = pyglet.image.load('img/robot/shoot.png')
intro_robot = pyglet.sprite.Sprite(image_robot_intro,x = -100, y = 10)
intro_robot.scale = 0.9

# cloud image intro
image_cloud1_intro = pyglet.image.load('img/map/blackcloud.png')
image_cloud2_intro = pyglet.image.load('img/map/blackcloud1.png')
cloud1_intro = pyglet.sprite.Sprite(image_cloud1_intro, batch = batch, x = 100, y = 200)
cloud2_intro = pyglet.sprite.Sprite(image_cloud2_intro, batch = batch, x = 500, y = 300)
cloud1_intro.scale = 0.5
cloud2_intro.scale = 0.5

cloud_list_intro = [cloud1_intro, cloud2_intro]
def cloud_random_intro(cloud_intro):
    if cloud_intro.x < -400:
        cloud_intro.x = random.randint(700, 1000)
        cloud_intro.y = random.randint(200, 350)
    cloud_intro.x -= 2

# Bonus image Intro
image_arrowsign_intro = pyglet.image.load('img/map/ArrowSign.png')
arrowsign_intro = pyglet.sprite.Sprite(image_arrowsign_intro, batch = batch, x = 350, y = 100)
arrowsign_intro.scale = 2


def draw_intro():
    intro_BG.draw()
    batch.draw()
    intro_zombie.draw()
    intro_robot.draw()
    label.draw()
    label1.draw()
    nameteam.draw()
