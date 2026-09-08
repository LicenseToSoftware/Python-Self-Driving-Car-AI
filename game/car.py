import pygame

class Car(pygame.sprite.Sprite):
    """Represents a car and its position in the game world."""
    MAX_SPEED = 3
    ACCELERATION = 0.03
    DRAG = 0.95

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

            self.speed = self.direction = 0

            # Car's velocity and drag properties
            self.position = pygame.Vector2(self.rect.center)
            self.velocity = pygame.Vector2(0, 0)

            self.acceleration_direction = pygame.Vector2(0, 0)  # Initialize acceleration_direction as a 2D vector

    def move(self, dx, dy):
        self.acceleration_direction.update(dx, dy)
        
    def update(self):
        """Move the car and gradually reduce its acceleration_direction."""

        # Update the car's position based on its velocity and acceleration direction
        if self.acceleration_direction.length_squared() > 0:
            direction = self.acceleration_direction.normalize()
            self.velocity += direction * self.ACCELERATION
        else:
            self.velocity *= self.DRAG
            
            # Stop completely once movement becomes very small.
            if self.velocity.length() < 0.1:
                self.velocity.update(0, 0)
        
        # Limit the car's speed to the maximum speed in both directions
        if self.velocity.length() > self.MAX_SPEED:
                self.velocity.scale_to_length(self.MAX_SPEED)



        # Update the car's position based on its velocity
        self.position += self.velocity
        self.rect.center = (round(self.position.x), round(self.position.y))




        # Clear the requested direction for the next frame.
        self.acceleration_direction.update(0, 0)