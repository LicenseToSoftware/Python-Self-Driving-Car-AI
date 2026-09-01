import pygame

class Car(pygame.sprite.Sprite):
    """    
    Represents a car in the game world.

    The car is a Pygame sprite with an image used for rendering
    and a rectangle used for positioning and collision detection.
    """

    def __init__(self, color, x, y):
        """
        Initialize a car with a color and starting position.

        Args:
            color: The color used to display the car.
            x (int): The starting x-coordinate of the car's center.
            y (int): The starting y-coordinate of the car's center.
        """
        super().__init__()
        # Set the car's color, size, and position
        self.image = pygame.Surface((25, 10))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)