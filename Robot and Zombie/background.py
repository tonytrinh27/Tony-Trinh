import pyglet
from pyglet.window import mouse
import random

#window = pyglet.window.Window(800, 600)
label = pyglet.text.Label(font_size=36, y=300, x=400)

# Goi ham thu vien co san
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

# background image
backgr = pyglet.image.load('img/map/BG.png')
BG = pyglet.sprite.Sprite(backgr, group = background)
BG.scale = 0.55

# cloud image
image_cloud1 = pyglet.image.load('img/map/blackcloud.png')
image_cloud2 = pyglet.image.load('img/map/blackcloud1.png')
cloud1 = pyglet.sprite.Sprite(image_cloud1, batch = batch, x = 100, y = 200)
cloud2 = pyglet.sprite.Sprite(image_cloud2, batch = batch, x = 500, y = 300)
cloud1.scale = 0.5
cloud2.scale = 0.5

cloud_list = [cloud1, cloud2]
def cloud_random(cloud):
    if cloud.x < -400:
        cloud.x = random.randint(700, 1000)
        cloud.y = random.randint(200, 350)
    cloud.x -= 2


def get_cloud_list():
    return cloud_list
# Bonus image
image_Stone1 = pyglet.image.load('img/map/TombStone (1).png')
image_Stone2 = pyglet.image.load('img/map/TombStone (2).png')
image_Tree = pyglet.image.load('img/map/Tree.png')
image_Sign = pyglet.image.load('img/map/Sign.png')
image_Skeleton = pyglet.image.load('img/map/Skeleton.png')


Stone1 = pyglet.sprite.Sprite(image_Stone1, batch = batch, x = 450, y = 30)
Stone2 = pyglet.sprite.Sprite(image_Stone2, batch = batch, x = 600, y = 160)
Tree = pyglet.sprite.Sprite(image_Tree, batch = batch, x = 200, y = 165)
Skeleton = pyglet.sprite.Sprite(image_Skeleton, batch = batch, x = 600, y = 35)



# Xu ly Ground
ground_left = pyglet.image.load('img/map/groundleft.png')
ground_mid = pyglet.image.load('img/map/groundmid.png')
ground_right = pyglet.image.load('img/map/groundright.png')


def sprite_ground(Y):
    ground_bot_left = pyglet.sprite.Sprite(ground_left, x=0, y=Y)
    ground_bot_right = pyglet.sprite.Sprite(ground_right, x=735, y=Y)
    group_list = []
    group_list.append(ground_bot_left)
    for x in range(1):
        for y in range(12):
            group_list.append(pyglet.sprite.Sprite(ground_mid,
                                        x=60+y*56, y=Y+x*10))
    group_list.append(ground_bot_right)
    for i in group_list:
        i.scale = 0.5
    return group_list




def draw_background():
    first_list = sprite_ground(-25)
    second_list = sprite_ground(100)
    BG.draw()
    batch.draw()
    for m in first_list:
        m.draw()
    for l in second_list:
        l.draw()
