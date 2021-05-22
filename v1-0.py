from pygame import *
game = True
clock = time.Clock()
FPS = 120
win = display.set_mode((700, 500))
display.set_caption("ping-pong")
class GameSprite(sprite.Sprite):
    def __init__(self, gamer_image,gamer_x, gamer_y, gamer_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(gamer_image),(size_x,size_y))
        self.speed = gamer_speed
        self.rect = self.image.get_rect()
        self.rect.x = gamer_x
        self.rect.y = gamer_y
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y <= 325:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LSHIFT] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if key_pressed[K_LCTRL] and self.rect.y <= 325:
            self.rect.y += self.speed

class Ball(GameSprite):
    speedb_x = 2
    speedb_y = 2

    def update(self):
        if finish != True:
            ball.rect.x += self.speedb_x
            ball.rect.y += self.speedb_y
        if ball.rect.y >= 450 or ball.rect.y <= 0:
            self.speedb_y *= -1
        if sprite.collide_rect(ball, rocket2) or sprite.collide_rect(ball, rocket1):
            self.speedb_x *= -1


global finish
finish = False

rocket1 = Player2('rocket1.png', 10, 190, 5 ,28, 166)
rocket2 = Player1('rocket1.png', 660, 190, 5 ,28, 166)
ball = Ball('ball.png', 330, 190, 5 ,50, 50)
place = transform.scale(image.load('place.png'),(700,500))
while game:
    clock.tick(FPS)
    win.blit(place,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != False:
        game = False

    rocket1.update()
    rocket1.reset()
    rocket2.update()
    rocket2.reset()
    ball.update()
    ball.reset()
    display.update()
