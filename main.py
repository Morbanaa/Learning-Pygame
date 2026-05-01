import pygame

GAME_WIDTH = 1000
GAME_HEIGHT = 1000

class Player():
    def __init__(self,xpos,ypos,speed):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed

# Set up window
pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
pygame.display.set_caption("Learning Pygame!")

# Create game objects
player = Player(GAME_WIDTH//2,GAME_HEIGHT//2,5)
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update

    #Controls WSAD
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.ypos -= player.speed
    if keys[pygame.K_s]:
        player.ypos += player.speed
    if keys[pygame.K_a]:
        player.xpos -= player.speed
    if keys[pygame.K_d]:
        player.xpos += player.speed

    # Draw
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0, 255, 0), (player.xpos , player.ypos), 10)
    pygame.display.update()
pygame.quit()

