import pygame

class Car(pygame.sprite.Sprite):
    """Represents a car and its position in the game world."""

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

            # Car's velocity and drag properties
            self.position = pygame.Vector2(self.rect.center)
            self.velocity = pygame.Vector2(0, 0)  # Initialize velocity as a 2D vector
            self.drag = 0.99

    def move(self, dx, dy):
        self.velocity.update(dx, dy)
        
    def update(self):
        """Move the car and gradually reduce its velocity."""
        self.position += self.velocity
        self.rect.center = (round(self.position.x), round(self.position.y))

        # Slow the car down gradually.
        self.velocity *= self.drag

        # Stop completely once movement becomes very small.
        if self.velocity.length() < 0.1:
            self.velocity.update(0, 0)