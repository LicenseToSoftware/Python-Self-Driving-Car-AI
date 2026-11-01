import pygame
import math

class Player_Controls:
    def __init__(self, car):
        self.car = car

    def player_movement(self, keys):
        """
        Set the car's acceleration direction based on player input.

        Args:
            keys: The current state of the keyboard.
            car: The car receiving the movement input.
        """
        forward = 0

        if keys[pygame.K_w]:
            forward += 1
        if keys[pygame.K_s]:
            forward -= 1

        angle = math.radians(self.car.angle)
        dx = math.cos(angle) * forward
        dy = math.sin(angle) * forward

        self.car.move(dx, dy)

    def player_steering(self, keys, dt):
        """
        Adjust the car's angle based on player input.
        """
        if keys[pygame.K_a]:
            self.car.angle -= self.car.TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.car.angle += self.car.TURN_SPEED * dt