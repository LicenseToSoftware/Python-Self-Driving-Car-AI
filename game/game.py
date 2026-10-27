import pygame

from game.car import Car
from input.human_controller import player_controls
from input.debug_controls import debug_controls
from debug.debug_overlay import draw_debug_overlay as debug_overlay


# Main Game loop and state managment
pygame.init()

# Debug
debug_overlay_enabled = False
debug_font = pygame.font.Font(None, 22)

# Display Settings
screen = pygame.display.set_mode((1280, 720))
screen_bounds = screen.get_rect()

#Timing
FPS_LIMIT = 60
clock = pygame.time.Clock()


# Game State
running = True

# Create Game Objects
carColor = "red"
car = Car(carColor, 600, 360)

#Add the car to the sprite group
cars = pygame.sprite.Group()
cars.add(car)

while running:
    # Calculate the time since the previous frame.
    dt = clock.tick(FPS_LIMIT) / 1000.0 

    # Process Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                debug_overlay_enabled = not debug_overlay_enabled

    # Process player inputs.
    keys = pygame.key.get_pressed()
    player_controls(keys, car)
    cars.update(screen_bounds, dt)  # Update the car's position after moving


    # update frame
    screen.fill("dark grey")
    cars.draw(screen)

    if debug_overlay_enabled:
        debug_overlay(screen, car, debug_font)


    # Display The frame
    pygame.display.flip()


pygame.quit()