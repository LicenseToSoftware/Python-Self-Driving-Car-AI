import pygame

class Car(pygame.sprite.Sprite):
    """Represents a car and its position in the game world."""
    MAX_SPEED = 180
    ACCELERATION = 108
    DRAG = 0.95
    STOP_SPEED = 1

    def __init__(self, color, x, y):
            """
            Initialize the car's appearance, position, and movement.

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
            self.velocity = pygame.Vector2(0, 0)

            self.acceleration_direction = pygame.Vector2(0, 0)  # Initialize acceleration_direction as a 2D vector

    def move(self, dx, dy):
        """
        Set the direction in which the car should accelerate.
        Args:
            dx (float): The x-component of the acceleration direction.
            dy (float): The y-component of the acceleration direction.
        """
        self.acceleration_direction.update(dx, dy)
        
    def update(self, bounds, dt):
        """"
        Update the car's position based on its velocity and acceleration direction.
        Args:
            bounds (pygame.Rect): The rectangular area within which the car should stay.
        """

        # Update the car's position based on its velocity and acceleration direction
        if self.acceleration_direction.length_squared() > 0:
            direction = self.acceleration_direction.normalize()

            # Apply acceleration in the direction of movement
            self.velocity += direction * self.ACCELERATION * dt
        else:
            self.velocity *= self.DRAG ** (dt * 60) 
            
        # Stop once the remaining velocity becomes negligible.
        if self.velocity.length() < self.STOP_SPEED:
            self.velocity.update(0, 0)
        
        # Limit the car's speed to the maximum speed in both directions
        if self.velocity.length() > self.MAX_SPEED:
                self.velocity.scale_to_length(self.MAX_SPEED)

        # Velocity is measured in pixels per second.
        # Multiplying it by dt gives the distance traveled this frame.
        self.position += self.velocity * dt

        # Synchronize the sprite rectangle with the precise position.
        self.rect.center = (
             round(self.position.x), 
             round(self.position.y)
             )

        # Clamp the car's position within the specified bounds
        self.keep_inside(bounds)


        # Clear the requested direction for the next frame.
        self.acceleration_direction.update(0, 0)

    def keep_inside(self, bounds):
        """Keep the car inside the bounds and stop it upon impact."""

        hit_boundary = (
            self.rect.left < bounds.left
            or self.rect.right > bounds.right
            or self.rect.top < bounds.top
            or self.rect.bottom > bounds.bottom
        )

        # Return the rectangle to the nearest valid position.
        self.rect.clamp_ip(bounds)

        # Keep the precise position synchronized with the rectangle.
        self.position.update(self.rect.center)

        if hit_boundary:
            self.velocity.update(0, 0)