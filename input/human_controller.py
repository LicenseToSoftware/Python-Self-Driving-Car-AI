import pygame

class Player_Controls:
    def __init__(self, car):
        self.car = car
        self.forward = 0

    def handle_movement_input(self, keys):
        """
        Set the car's acceleration direction based on player input.

        Args:
            keys: The current state of the keyboard.
        """
        self.forward = 0

        if keys[pygame.K_w]:
            self.forward += 1
        if keys[pygame.K_s]:
            self.forward -= 1
        
        self.car.set_movement_input(self.forward)


    def handle_steering_input(self, keys, dt):
        """
        Adjust the car's angle based on player input.
        """

        direction = 0
        if keys[pygame.K_a]:
            direction -= 1
        if keys[pygame.K_d]:
            direction += 1
            
        self.car.steer(direction, dt)

    def handle_player_input(self, keys, dt):
        """
        Handle both movement and steering input for the car.
        Args:
            keys: The current state of the keyboard.
            dt: The time delta since the last frame.
        """
        self.handle_steering_input(keys, dt)
        self.handle_movement_input(keys)
