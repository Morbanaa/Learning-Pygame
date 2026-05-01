import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Learning Pygame!")

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update


    # Draw
    screen.fill((255,255,255))
    pygame.display.update()
pygame.quit()

