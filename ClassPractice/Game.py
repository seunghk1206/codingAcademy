import pygame # pip install pygame!

pygame.init()

class player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.isJump = False
        self.JumpCount = 10
        self.standing = True
        self.hitbox = (self.x +17, self.y+11, 28, 60)

    def draw(self, screen):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                screen.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            else:
                screen.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x +17, self.y+11, 29, 52)
    
    def hit(self):
        self.JumpCount = 10
        self.isJump = False
        self.x = 50
        self.y = 400
        self.walkCount = 0

        msg = pygame.font.SysFont('comicsans', 100)
        text = msg.render('Dead', 1, (255,0,0))
        screen.blit(text, (300-(text.get_width()/2), 200))
        pygame.display.update()
        i = 0
        while i<100:
            pygame.time.delay(10)
            i += 1
            for eachEvent in pygmae.event.get():
                if eachEvent.type == pygame.QUIT:
                    pygame.quit()
    
class projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 25 * facing
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class portal():
    dungeonPortal = [pygame.image.load('door/door_n.png'), pygame.image.load('door/door_m.png')]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, screen):
        if beginning == 1:
            screen.blit(self.dungeonPortal[0], (self.x, self.y))
        elif second == 1:
            screen.blit(self.dungeonPortal[1], (self.x, self.y))

class npc:
    standing = pygame.image.load('Game/Standing.png')
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, screen):
        screen.blit(self.standing, (self.x, self.y))
    def dialogue(self, writings):
        self.writings = writings
        dia = dia_font.render(self.writings, 25, (255, 0, 0))

        screen.blit(dia, (200, 410))

