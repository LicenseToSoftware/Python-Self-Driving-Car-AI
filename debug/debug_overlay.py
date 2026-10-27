import pygame

def draw_debug_overlay(screen, car, font):
    """
    Draw a debug overlay on the screen, showing the car's position, orientation, and other relevant information.
    Args:
        screen (pygame.Surface): The surface on which to draw the overlay.
        car (Car): The car object whose information is to be displayed.
        font (pygame.font.Font): The font used for rendering text.
    """

    width, height = screen.get_size()
    grid_spacing = 100

    # Draw the coordinate grid.
    # Draw vertical lines and label them with their x-coordinates.
    for x in range(0, width, grid_spacing):
        pygame.draw.line(
            screen,
            "dimgray",
            (x, 0),
            (x, height),
            1,
        )

        label_x = font.render(str(x), True, "white")
        screen.blit(label_x, (x + 3, 3))

    # Draw horizontal lines and label them with their y-coordinates.
    for y in range(0, height, grid_spacing):
        pygame.draw.line(
            screen,
            "dimgray",
            (0, y),
            (width, y),
            1,
        )
        
        label_y = font.render(str(y), True, "white")
        screen.blit(label_y, (3, y + 3))

    # Use the car's precise center position.
    center = pygame.Vector2(car.position)

    # Calculate which direction the front is pointing.
    forward = pygame.Vector2(1, 0).rotate(-car.angle)

    # The car is 25 pixels long.
    half_length = car.original_image.get_width() / 2

    front = center + forward * half_length
    rear = center - forward * half_length

    # Draw the sprite's rectangular boundary.
    pygame.draw.rect(screen, "yellow", car.rect, 1)

    # Draw the center.
    pygame.draw.circle(screen, "white", center, 4)

    # Draw a line from the center toward the front.
    pygame.draw.line(
        screen,
        "lime",
        center,
        front,
        3,
    )

    # Mark the front and rear.
    pygame.draw.circle(screen, "lime", front, 5)
    pygame.draw.circle(screen, "red", rear, 5)

    # Label the important points.
    center_label = font.render(
        f"Center ({center.x:.1f}, {center.y:.1f})",
        True,
        "white",
    )

    front_label = font.render(
        f"Front ({front.x:.1f}, {front.y:.1f})",
        True,
        "lime",
    )

    rear_label = font.render(
        f"Rear ({rear.x:.1f}, {rear.y:.1f})",
        True,
        "red",
    )

    screen.blit(center_label, center + pygame.Vector2(10, -35))
    screen.blit(front_label, front + pygame.Vector2(10, -10))
    screen.blit(rear_label, rear + pygame.Vector2(10, 10))

    # Show the car's angle and forward vector.
    angle_text = font.render(
        f"Angle: {car.angle:.1f} degrees",
        True,
        "white",
    )

    forward_text = font.render(
        f"Forward: ({forward.x:.2f}, {forward.y:.2f})",
        True,
        "white",
    )

    screen.blit(angle_text, (10, height - 55))
    screen.blit(forward_text, (10, height - 30))

    # Show the mouse position.
    mouse_x, mouse_y = pygame.mouse.get_pos()

    pygame.draw.line(
        screen,
        "cyan",
        (mouse_x - 8, mouse_y),
        (mouse_x + 8, mouse_y),
    )

    pygame.draw.line(
        screen,
        "cyan",
        (mouse_x, mouse_y - 8),
        (mouse_x, mouse_y + 8),
    )

    mouse_text = font.render(
        f"Mouse: ({mouse_x}, {mouse_y})",
        True,
        "cyan",
    )

    screen.blit(mouse_text, (mouse_x + 12, mouse_y + 12))