import pygame, random
pygame.init
pygame.font.init()
pygame.mixer.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
W, H = pygame.display.get_window_size()
menu_image = pygame.image.load('menu.png')
menu_image = pygame.transform.scale(menu_image,(W,H))
size = 64
FPS = 900
ball_image = pygame.image.load('ball.png')
ball_image = pygame.transform.scale(ball_image,(size,size))
clock = pygame.time.Clock()
game = True
Wsize = W//size
Hsize = H//size
class Base():
    def __init__(self,x,y,image,speed):
        self.hitbox = image.get_rect(topleft = (x,y))
        self.image = image
        self.speed = speed
    def draw(self):
        window.blit(self.image, self.hitbox)
class Ball(Base):
    def __init__(self, x, y, image, speed):
        super().__init__(x, y, image, speed,)
        self.speed_x = speed
        self.speed_y = speed
    def move(self):
        self.hitbox.x += self.speed_x
        self.hitbox.y += self.speed_y
        if self.hitbox.right >= W:
            self.speed_x = -self.speed
        if self.hitbox.left <= 0:
            self.speed_x = self.speed
        if self.hitbox.bottom >= H:
            self.speed_y = -self.speed
        if self.hitbox.top <= 0:
            self.speed_y = self.speed
ball = Ball(W//2,H//2,ball_image,10)



while game == True:
    window.blit(menu_image,(0,0))
    event_list = pygame.event.get()
    key_list = pygame.key.get_pressed()
    for event in event_list:
        if event.type == pygame.QUIT:
            game = False
    window.blit(ball_image,ball.hitbox)
    ball.move()
    clock.tick(FPS)
    pygame.display.update()