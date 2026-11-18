import pygame


class DebugOverlay:
    """Draw debug information for the car simulation."""

    def __init__(self, screen, car, font):
        self.screen = screen
        self.car = car
        self.font = font

    def draw(self):
        self.draw_grid()
        self.draw_car_debug_overlay()
        self.draw_mouse_debug_overlay()
        self.draw_screen_bounds()

    def draw_grid(self):
        width, height = self.screen.get_size()
        grid_spacing = 100

        for x in range(0, width, grid_spacing):
            pygame.draw.line(self.screen, "dimgray", (x, 0), (x, height), 1)
            label_x = self.font.render(str(x), True, "white")
            self.screen.blit(label_x, (x + 3, 3))

        for y in range(0, height, grid_spacing):
            pygame.draw.line(self.screen, "dimgray", (0, y), (width, y), 1)
            label_y = self.font.render(str(y), True, "white")
            self.screen.blit(label_y, (3, y + 3))

    def draw_car_debug_overlay(self):
        width, height = self.screen.get_size()
        center = pygame.Vector2(self.car.position)
        forward = pygame.Vector2(1, 0).rotate(self.car.angle)
        half_length = self.car.original_image.get_width() / 2
        front = center + forward * half_length
        rear = center - forward * half_length

        pygame.draw.rect(self.screen, "yellow", self.car.rect, 1)
        pygame.draw.circle(self.screen, "white", center, 4)
        pygame.draw.line(self.screen, "lime", center, front, 3)
        pygame.draw.circle(self.screen, "lime", front, 5)
        pygame.draw.circle(self.screen, "red", rear, 5)

        center_label = self.font.render(
            f"Center ({center.x:.1f}, {center.y:.1f})", True, "white"
        )
        front_label = self.font.render(
            f"Front ({front.x:.1f}, {front.y:.1f})", True, "lime"
        )
        rear_label = self.font.render(
            f"Rear ({rear.x:.1f}, {rear.y:.1f})", True, "red"
        )
        self.screen.blit(center_label, center + pygame.Vector2(10, -35))
        self.screen.blit(front_label, front + pygame.Vector2(10, -10))
        self.screen.blit(rear_label, rear + pygame.Vector2(10, 10))

        velocity_text = self.font.render(
            f"Velocity: ({self.car.velocity.x:.1f}, {self.car.velocity.y:.1f})",
            True,
            "white",
        )
        angle_text = self.font.render(
            f"Angle: {self.car.angle:.1f} degrees", True, "white"
        )
        forward_text = self.font.render(
            f"Forward: ({forward.x:.2f}, {forward.y:.2f})", True, "white"
        )
        self.screen.blit(velocity_text, (10, height - 80))
        self.screen.blit(angle_text, (10, height - 55))
        self.screen.blit(forward_text, (10, height - 30))

    def draw_mouse_debug_overlay(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.line(
            self.screen, "cyan", (mouse_x - 8, mouse_y), (mouse_x + 8, mouse_y)
        )
        pygame.draw.line(
            self.screen, "cyan", (mouse_x, mouse_y - 8), (mouse_x, mouse_y + 8)
        )

        mouse_text = self.font.render(
            f"Mouse: ({mouse_x}, {mouse_y})", True, "cyan"
        )
        self.screen.blit(mouse_text, (mouse_x + 12, mouse_y + 12))

    def draw_screen_bounds(self):
        width, height = self.screen.get_size()
        pygame.draw.rect(
            self.screen, "red", (0, 0, width, height), 2
        )  # Draw a red rectangle around the screen bounds

