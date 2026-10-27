import pygame
def debug_controls(event, debug_enabled):
    """
    Handle debug controls based on the current state of the keyboard.
    """

    # Toggle debug overlay visibility
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
            return not debug_enabled