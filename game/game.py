import pygame

from game.car import Car
from input.human_controller import player_controls


# Main Game loop and state managment
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Load Game Assets once
# Load Cars
carColor = "red"
cars = pygame.sprite.Group()
car = Car(carColor, 600, 360)
#Add the car to the sprite group
cars.add(car)

while running:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_controls(keys, car)
    car.update()  # Update the car's position after moving



    # update screen
    screen.fill("dark grey")
    cars.draw(screen)

    # RENDER YOUR GAME HERE


    #draw rects

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()