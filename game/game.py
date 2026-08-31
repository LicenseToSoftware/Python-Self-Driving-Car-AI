import pygame

from car import Car

# Maine Game loop and state managment
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Load Game Assets once
car = Car(350, 250, 25, 10)

while running:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("dark grey")

    # RENDER YOUR GAME HERE
    #draw rects
    pygame.draw.rect(screen, car.carColorRed, car.rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()