import pygame
import math

class Car(pygame.sprite.Sprite):
    """Represents a car and its position in the game world.
    Attributes:
        original_image: The car image before rotation.
        image: The current image shown on screen.
        rect: The rectangle used to position the image.
        position: The car's precise position.
        velocity: The car's current velocity.
        acceleration_direction: The direction the car is accelerating.
        angle: The car's heading in degrees; 0 faces right.
        """
    MAX_SPEED = 180
    MIN_STEERING_SPEED = 25
    ACCELERATION = 108
    DRAG = 0.95
    STOP_SPEED = 1
    TURN_SPEED = 90  # Degrees per second

    def __init__(self, car_image_path, x, y):
            """
            Initialize the car's appearance, position, and movement.

            Args:
                car_image_path (str): The file path to the car image.
                x (int): The starting x-coordinate of the car's center.
                y (int): The starting y-coordinate of the car's center.
            """
            super().__init__()
            # Set the car's color, size, and position

            # Create and preserve the car's original unrotated image.
            self.original_image = pygame.image.load(car_image_path)
            self.image = self.original_image
            self.rect = self.image.get_rect(center=(x, y))

            # This image can later be rotated for display.
            self.image = self.original_image.copy()

            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

            # Car's velocity and drag properties
            self.position = pygame.Vector2(self.rect.center)
            self.velocity = pygame.Vector2(0, 0)

            self.acceleration_direction = pygame.Vector2(0, 0)  # Initialize acceleration_direction as a 2D vector

            # The car's angle in degrees, where 0 is facing right.
            self.angle = 0
            
    def set_movement_input(self, forward):
        """
        Set the direction in which the car should accelerate.
        Args:
            forward (int): The forward/backward input from the player.
        """
        angle = math.radians(self.angle) # Must use local variable to avoid modifying the class attribute directly
        dx = math.cos(angle) * forward
        dy = math.sin(angle) * forward
        self.acceleration_direction.update(dx, dy)

    def steer(self, direction, dt):
        """
        Adjust the car's angle based on player input.
        Args:
            direction (int): The direction to steer; -1 for left, 1 for right.
            dt (float): The time delta since the last frame.
        """
        speed = self.velocity.length()

        if speed < self.MIN_STEERING_SPEED:
            return  # Don't steer if the car is nearly stopped
        
        self.angle += direction * self.TURN_SPEED * dt
        
    def update(self, bounds, dt):
        """
        Update the car's position based on its velocity and acceleration direction.
        Args:
            bounds (pygame.Rect): The rectangular area within which the car should stay.
        """
        self._update_velocity(dt)
        self._update_position(dt)
        self._update_image(bounds)

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
        
    def _update_position(self, dt):
        """
        Update the car's position based on its velocity and acceleration direction.
        Args:
            dt (float): The time delta since the last frame.
        """
        # Update the car's position based on its velocity and the time delta.
        self.position += self.velocity * dt


    def _update_velocity(self, dt):
        """
        Update the car's velocity based on its acceleration direction and drag.
        Args:
            dt (float): The time delta since the last frame.
        """

        # If the car is accelerating, apply acceleration in the direction of movement.
        if self.acceleration_direction.length_squared() > 0:
            direction = self.acceleration_direction.normalize()
            self.velocity += direction * self.ACCELERATION * dt
        else:
            # Apply drag to slow the car down when not accelerating.
            self.velocity *= self.DRAG ** (dt * 60) 

        # If the car's speed is below the stop threshold, set it to zero.
        if self.velocity.length() < self.STOP_SPEED:
            self.velocity.update(0, 0)
        
        # Clamp the car's speed to the maximum allowed speed.
        if self.velocity.length() > self.MAX_SPEED:
                self.velocity.scale_to_length(self.MAX_SPEED)

    def _update_image(self, bounds):
        """
        Update the car's image and rectangle based on its current angle and position.
        Args:
            bounds (pygame.Rect): The rectangular area within which the car should stay.
        """
        self.image = pygame.transform.rotate(self.original_image, -self.angle)

        # Keep the rotated image centered on the car's position.
        self.rect = self.image.get_rect(
            center=(round(self.position.x), round(self.position.y))
    )
        # Clamp the car's position within the specified bounds
        self.keep_inside(bounds)


        # Clear the requested direction for the next frame.
        self.acceleration_direction.update(0, 0)