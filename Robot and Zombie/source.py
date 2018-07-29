import pyglet
from pyglet.window import mouse
from pyglet.window import key
import background as bg
import intro as it
from random import randint

window = pyglet.window.Window(width=800, height=600, caption="hoos", resizable=False)
window.set_location(400, 300)
#fps_display = FPSDisplay(window)
#fps_display.label.font_size = 50
batch = pyglet.graphics.Batch()


# load images
# load the bullet
bullet = pyglet.image.load('img/bullet.png')
pow_bullet = pyglet.image.load('img/pow.png')

# list contain robot animation
robot = []
# append stand animation into list
for i in range(1,7):
    temp = pyglet.image.load('img/robot/stand'+str(i)+'.png')
    sprite_temp = pyglet.sprite.Sprite(temp,
                        x = 50, y = 30)
    sprite_temp.scale = 0.2
    robot.append(sprite_temp)
# append dead animation into list
for i in range(1,7):
    temp = pyglet.image.load('img/robot/dead'+str(i)+'.png')
    sprite_temp = pyglet.sprite.Sprite(temp,
                        x = 50, y = 30)
    sprite_temp.scale = 0.2
    robot.append(sprite_temp)
# append jump animation into list
for i in range(1,7):
    temp = pyglet.image.load('img/robot/jump'+str(i)+'.png')
    sprite_temp = pyglet.sprite.Sprite(temp,
                        x = 50, y = 30)
    sprite_temp.scale = 0.2
    robot.append(sprite_temp)
# and fire
shoot_img = pyglet.image.load('img/robot/shoot.png')
shoot_sprite = pyglet.sprite.Sprite(shoot_img,
                    x = 50, y = 30)
shoot_sprite.scale = 0.2
robot.append(shoot_sprite)
# after that, robot[0:5] is stand,
# robot[6:11] is dead and robot[12:17] is jump
# load sprite animation for bang
bang_image = pyglet.image.load('img/banghit.png')
bang_seq = pyglet.image.ImageGrid(bang_image, 4, 5, item_width=96, item_height=96)
bang_tex = pyglet.image.TextureGrid(bang_seq)
bang_anim = pyglet.image.Animation.from_image_sequence(bang_tex[0:], 0.1, loop=True)


# creating a label score
text2 = pyglet.text.Label("score: ", x=600 , y=550, batch=batch, color = (0, 255, 255, 255))
text2.italic = True
text2.bold = True
text2.font_size = 16

final_score = pyglet.text.Label(x=100 , y=400, color = (0, 255, 255, 255),font_size = 40)

health = pyglet.text.Label("health: 5", x=100 , y=550, batch=batch, color = (0, 255, 255, 255))
health.italic = True
health.bold = True
health.font_size = 16

intro_text = pyglet.text.Label("press space to start", x=400 , y=300)
intro_text.anchor_x = "center"
intro_text.anchor_y = "center"
intro_text.italic = True
intro_text.bold = True
intro_text.font_size = 30


bang_sound = pyglet.media.load('sounds/bang.wav', streaming=False)
shoot_sound = pyglet.media.load('sounds/shoot.wav', streaming=False)
# position of robot
x, y = 50, 30
fire_rate = 0
pow_fire = False
up = False
down = False
speed = 500
score = 0
fire = False
robot_health = 5
robot_is_alive = True
game = False
counter = 0
hight = 0
bang_time = 2
lock = False # to lock counter
lock_jump = 0


# list
bullet_list = []
pow_bullet_list = []
zombie_list = []
dino_list = []
bang_list = []


# list
bullet_list = []
pow_bullet_list = []
zombie_list = []
dino_list = []
bang_list = []


def RePlay():
    global  x, y, fire_rate, pow_fire, up, down, speed
    global score, fire, robot_health, robot_is_alive, game550
    global counter, hight, bang_time, lock
    x, y = 50, 30
    fire_rate = 0
    pow_fire = False
    up = False
    down = False
    speed = 500
    score = 0
    fire = False
    robot_health = 5
    robot_is_alive = True
    game = False
    counter = 0
    hight = 0
    bang_time = 2
    lock = False # to lock counter
    zombie_list.clear()
    dino_list.clear()


@window.event
def on_draw():
    global counter, robot_is_alive
    window.clear()
    if game:
        if robot_is_alive:
            bg.draw_background()
            batch.draw()
            robot[int(counter)].draw()
            for z in zombie_list:
                z.draw()
            for d in dino_list:
                d.draw()
        # robot dead, end game
        else:
            bg.draw_background()
            final_score.text = "Final score: " + str(score)
            final_score.draw()
    else:
        it.draw_intro()


@window.event
def on_mouse_press(x, y, button, modifiers):
    print(x, y)

@window.event
def on_text_motion(motion):
    pass


@window.event
def on_key_press(symbol, modifiers):
    global  up, down, fire, game, counter, y, pow_fire, robot_is_alive
    if symbol == key.R:
        RePlay()
    if symbol == key.Q:
        game = False
    if symbol == key.UP:
        up = True
    if symbol == key.DOWN:
        down = True
    if symbol == key.ENTER:
        pow_fire = True
        counter = 15
    if symbol == key.SPACE:
        fire = True
        counter = 18
        robot[int(counter)].y = y
        y = robot[int(counter)].y
        if not game:
            game = True
            fire = False


@window.event
def on_key_release(symbol, modifiers):
    global  up, down, fire, counter, pow_fire
    if symbol == key.UP:
        #up = False
        pass
    if symbol == key.DOWN:
        #down = False
        pass
    if symbol == key.ENTER:
        pow_fire = False
        counter = 0
    if symbol == key.SPACE:
        counter = 0
        fire = False


def get_zombie_anim():
    zombie_anim = []
    for i in range(1,12):
        zombie_anim.append(pyglet.image.load('img/zombie/zombie'+str(i)+'.png'))
    return pyglet.image.Animation.from_image_sequence(zombie_anim, 0.1, True)


def get_dino_anim():
    dinor_anim = []
    for i in range(1,9):
        dinor_anim.append(pyglet.image.load('img/dino/run'+str(i)+'.png'))
    return pyglet.image.Animation.from_image_sequence(dinor_anim, 0.1, True)


def create_enemy():
    choiceX = randint(1,6)
    x_rand = 800 + choiceX*100
    choice = randint(0,1)
    y_rand = 30 + choice*130
    d_or_z = randint(1,5)
    if d_or_z > 2:
        if len(zombie_list) < 10:
            zombie_list.append(pyglet.sprite.Sprite(get_zombie_anim(),x = x_rand,y = y_rand))
    else:
        if len(dino_list) < 10:
            dino_list.append(pyglet.sprite.Sprite(get_dino_anim(),x = x_rand,y = y_rand))
    for i in zombie_list:
        i.scale = 0.15
    for i in dino_list:
        i.scale = 0.2


def enemy_move(zombies,dinos, zspeed, dt):
    for zom in zombies:
        zom.x -= zspeed*dt
    for di in dinos:
        di.x -= zspeed*dt*3


# when enemy get hit
def zombie_hit(zombie):
    global score
    bang_list.append(pyglet.sprite.Sprite(bang_anim, x=zombie.x, y=zombie.y, batch=batch))
    zombie_list.remove(zombie)
    score += 1


def dino_hit(dino):
    global score
    bang_list.append(pyglet.sprite.Sprite(bang_anim, x=dino.x, y=dino.y, batch=batch))
    dino_list.remove(dino)
    score += 2


def is_collision(zombies, dinos):
    global x, y
    for zom in zombies:
        if zom.x <= x and abs(zom.y - y) <= 50:
            zombies.remove(zom)
            return True
    for dino in dinos:
        if dino.x <= x and abs(dino.y - y) <= 50:
            dinos.remove(dino)
            return True


def robot_hit():
    global robot_health, robot_is_alive
    robot_health -= 1
    global x, y
    X, Y = x, y
    bang_list.append(pyglet.sprite.Sprite(bang_anim, x = X, y = Y, batch=batch))
    if robot_health <= 0:
        robot_is_alive = False



def robot_jump(dt):
    global counter, x, y, hight, lock
    global up, down, lock_jump
    #counter = 12
    if up:
        if counter > 17:
            counter = 12
        counter += 4*dt
        robot[int(counter)].y = y
        robot[int(counter)].y += 160*dt
        hight += 160 *dt
        #print("rs: ", y, int(counter), robot[int(counter)].y)
        if hight > 130:
            hight = 0
            up = False
            lock = False
            counter = 0
            lock_jump = 1
            robot[int(counter)].y = y
    if down:
        if counter > 17:
            counter = 12
        counter += 4*dt
        robot[int(counter)].y = y
        robot[int(counter)].y -= 160*dt
        hight += 160 *dt
        #print("rs: ", y, int(counter), robot[int(counter)].y)
        if hight > 130:
            hight = 0
            down = False
            lock = False
            counter = 0
            lock_jump = 0
            robot[int(counter)].y = y
    y = robot[int(counter)].y

def pow_fire_shoot(dt):
    global pow_fire, counter
    pow_bullet_list.append(pyglet.sprite.Sprite(pow_bullet,
     x = robot[int(counter)].x + 60, y = robot[int(counter)].y-50, batch=batch))
    pow_fire = False


def update_pow_bullet(dt):
    for pb in pow_bullet_list:
        pb.x += 600*dt
        if pb.x > 1000:
            pow_bullet_list.remove(pb)

def robot_shoot(dt):
    global fire_rate, counter, pow_fire
    fire_rate -= dt
    if fire_rate <= 0:
        bullet_sprite = pyglet.sprite.Sprite(bullet, robot[int(counter)].x + 60,
        robot[int(counter)].y+43, batch=batch)
        bullet_sprite.scale = 0.1
        bullet_list.append(bullet_sprite)
        fire_rate += 0.2
        if robot_is_alive:
            pass
            #shoot_sound.play()


def update_shoot(dt):
    for bull in bullet_list:
        bull.x += 1500*dt
        if bull.x > 1000:
            bullet_list.remove(bull)


def bullet_collision(enemy, bullet_list):
    for b in bullet_list:
        if b.x >= enemy.x and abs(b.y - enemy.y) <= 50:
            bullet_list.remove(b)
            #bang_sound.play()
            return True


def pow_bullet_collision(enemy, pow_bullet_list):
    for b in pow_bullet_list:
        if b.x >= enemy.x and abs(b.y - enemy.y) <= 150:
            #pow_bullet_list.remove(b)
            #bang_sound.play()
            return True


def update_bang():
    global bang_time
    bang_time -= 0.05
    if bang_time <= 0:
        for b in bang_list:
            bang_list.remove(b)
            b.delete()
        bang_time += 2


def updategame(dt):
    global counter,lock, score, robot_is_alive
    if game:
        create_enemy()
        enemy_move(zombie_list, dino_list, 30, dt)
        for zom in zombie_list:
            if bullet_collision(zom, bullet_list):
                zombie_hit(zom)
            if pow_bullet_collision(zom, pow_bullet_list):
                zombie_hit(zom)
        for dino in dino_list:
            if bullet_collision(dino, bullet_list):
                dino_hit(dino)
            if pow_bullet_collision(dino, pow_bullet_list):
                dino_hit(dino)
        if is_collision(zombie_list, dino_list):
            robot_hit()
            update_bang()
        if up:
            if not lock:
                lock = True
                counter = 12
            robot_jump(dt)
        if down:
            if not lock:
                lock = True
                counter = 12
            robot_jump(dt)
        if fire:
            robot_shoot(dt)
        update_shoot(dt)
        update_bang()
        text2.text = "score: " + str(score)
        health.text = "health: " + str(robot_health)
        if pow_fire:
            pow_fire_shoot(dt)
        update_pow_bullet(dt)
        for cloud in bg.get_cloud_list():
            bg.cloud_random(cloud)


pyglet.clock.schedule_interval(updategame, 1.0/60)
pyglet.app.run()
