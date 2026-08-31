import pygame

class Car:
    """Represents a car and its position in the game world."""

    def __init__(self, x, y, widt, height):
        # Use one rectangle to track the car's position, size, and collisions.
        self.rect = pygame.Rect(x, y, widt, height)
        self.carColorRed = (255, 0, 0)