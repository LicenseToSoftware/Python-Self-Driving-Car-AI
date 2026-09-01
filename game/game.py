import pygame

from car import Car

# Main Game loop and state managment
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Load Game Assets once
# Load Cars
carColor = "red"  # Red color for the car TODO: Make this a parameter for the Car class
cars = pygame.sprite.Group()
car = Car(carColor, 600, 360)
#Add the car to the sprite group
cars.add(car)

while running:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update screen
    screen.fill("dark grey")
    cars.draw(screen)

    # RENDER YOUR GAME HERE
    #draw rects

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()