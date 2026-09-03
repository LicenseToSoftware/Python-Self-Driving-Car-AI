import pygame

def player_controls(keys, car):
    """
    Handle the game controls for moving the car based on key presses.

    Args:
        keys: The current state of all keyboard keys.
        car: The car object to be moved.
    """
    speed = 2  # Define the speed at which the car moves
    if keys[pygame.K_a]:
        car.move(-speed, 0)  # Move left
    if keys[pygame.K_d]:
        car.move(speed, 0)  # Move right
    if keys[pygame.K_w]:
        car.move(0, -speed)  # Move up
    if keys[pygame.K_s]:
        car.move(0, speed)  # Move down