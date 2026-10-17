import pygame

def player_controls(keys, car):
    """
    Send the player's requested movement direction to the car.

    Args:
        keys: The current state of the keyboard.
        car: The car receiving the movement input.
    """
    dx = 0
    dy = 0

    if keys[pygame.K_a]:
        dx -= 1
    if keys[pygame.K_d]:
        dx += 1
    if keys[pygame.K_w]:
        dy -= 1
    if keys[pygame.K_s]:
        dy += 1

    car.move(dx, dy)
    #Fixme code comment return
    return dx, dy