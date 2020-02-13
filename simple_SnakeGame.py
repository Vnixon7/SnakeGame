import pygame
import random

win_w = 500
win_h = 500

# initiating the use of system font and pygame#
pygame.font.init ()
pygame.init ()

# FPS
clock = pygame.time.Clock ()
# initiating game window/surface
window = pygame.display.set_mode ((win_w, win_h))

# specifying fonts to use
fontL = pygame.font.SysFont ('comicansms', 80)
fontS = pygame.font.SysFont ('comicansms', 30)


class snake (object):
    def __init__(self, color, height, width):

        self.color = color
        self.height = height
        self.width = width
        self.dx = 0
        self.dy = 0
        self.count = 0
        self.vel = 10
        self.snake_head = [250, 250]
        self.snake_position = [self.snake_head, [240, 250], [230, 250]]
        self.timer = 0

    # drawing snake to surface as rect#
    def draw(self, window):
        for pos in self.snake_position:
            pygame.draw.rect (window, self.color, (pos[0], pos[1], self.height, self.width))

    # returning x,y coordinate and height and width#
    def getRec(self):
        return pygame.Rect (self.snake_head[0], self.snake_head[1], self.width, self.height)

    # Checking collision with food#
    def ate(self):
        if food.getRec ().colliderect (self.getRec ()):
            self.snake_position.insert (0, list (self.snake_head))
            self.count = self.count + 1
            self.timer = 0

    # drawing score to surface#
    def score(self):
        score = fontS.render ('SCORE: ' + str (self.count), True, (0, 0, 0))
        window.blit (score, (0, 0))

    # checking collision with outer surface#
    def death(self):

        if self.snake_head[0] > win_w - self.width or self.snake_head[0] < 0 + self.width or self.snake_head[
            1] > win_h - self.height or self.snake_head[1] < 0 + self.height:
            youLose = fontL.render ('YOU LOST', True, (0, 0, 0))
            restart = fontS.render ('Click R to restart', True, (0, 255, 0))
            window.blit (restart, (170, 240))
            window.blit (youLose, (120, 180))
            self.vel = 0
            self.count = 0
            self.timer = 0

    # checking collision with self#
    def collision_self(self):
        self.timer = self.timer + 1
        head = self.snake_position[0]
        if head in self.snake_position[1:] and self.timer > 5:
            youLose = fontL.render ('YOU LOST', True, (0, 0, 0))
            restart = fontS.render ('Click R to restart', True, (0, 255, 0))
            window.blit (restart, (170, 240))
            window.blit (youLose, (120, 180))
            self.vel = 0
            self.count = 0

    # getting visual of numbers
    def dis_from_edge(self):

        if self.dx == -1:
            print ('Your distance from Left edge: ', self.snake_head[0] + 0)
        if self.dx == 1:
            print ('Your distance from Right edge: ', self.snake_head[0] - win_w)
        if self.dy == -1:
            print ('Your distance from Top edge: ', self.snake_head[1] + 0)
        if self.dy == 1:
            print ('Your distance from the Bottom edge: ', self.snake_head[1] - win_h)

    def dis_from(self, dis1, dis2):

        xydis = (self.snake_head[0] - dis1), (self.snake_head[1] - dis2)
        return xydis


class food (object):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = x
        self.height = height
        self.width = width

    # drawing food to surface#
    def draw(self, window):
        pie = pygame.image.load ('pie4.jpg')
        pie = pygame.transform.scale (pie, (self.width, self.height))
        window.blit (pie, (self.x, self.y))

    # getting x,y coordinate and width,height
    def getRec(self):
        return pygame.Rect (self.x, self.y, self.width, self.height)

    # checking collision with snake
    def ate(self):
        if main.getRec ().colliderect (self.getRec ()):
            self.x = random.randint (50, 450)
            self.y = random.randint (50, 450)


# used to reset after gameover#
def reset():
    main.vel = 10
    main.snake_head[0] = 250
    main.snake_head[1] = 250
    main.dx = 0
    main.dy = 0
    main.timer = 0
    ### deleting body ###
    for pos in main.snake_position:
        pos.pop ()
        pos.pop ()
    ### spawning original body###
    main.snake_head = [250, 250]
    main.snake_position = [main.snake_head, [240, 250], [230, 250]]


# drawing everything to surface#
def draw_window():
    window.fill ((255, 255, 255))
    main.collision_self ()
    main.ate ()
    food.ate ()
    main.death ()
    main.draw (window)
    main.score ()
    food.draw (window)

    pygame.display.update ()


main = snake ((0, 0, 0), 12, 12)
food = food (30, 300, 24, 24)

run = True
while run:

    main.timer = main.timer + 1
    # starting direction and continuous movement#
    if main.dx == 0 and main.dy == 0:
        main.snake_head[0] += main.vel
    # inserting new snake head and deleting the tale for movement
    main.snake_position.insert (0, list (main.snake_head))
    main.snake_position.pop ()

    clock.tick (13)
    keys = pygame.key.get_pressed ()
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit ()
            quit ()

        # if event.type == pygame.KEYUP:
        # print ('Distance from food:', main.dis_from (food.x, food.y))
        # print ('Distance from edge:', main.dis_from (win_w, win_h))
    # Specifying keys for movement#
    if keys[pygame.K_LEFT]:
        main.dx = -1
        main.dy = 0

    if keys[pygame.K_RIGHT]:
        main.dx = 1
        main.dy = 0

    if keys[pygame.K_UP]:
        main.dy = -1
        main.dx = 0

    if keys[pygame.K_DOWN]:
        main.dy = 1
        main.dx = 0

    if keys[pygame.K_r]:
        reset ()

    if main.dx == -1:
        main.snake_head[0] -= main.vel
    if main.dx == 1:
        main.snake_head[0] += main.vel
    if main.dy == -1:
        main.snake_head[1] -= main.vel
    if main.dy == 1:
        main.snake_head[1] += main.vel

    draw_window ()
