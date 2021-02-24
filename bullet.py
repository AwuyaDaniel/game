
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class to manage bullet fired from the ship"""
    def __init__(self, ai_settings, screen, ship):
        """Create bullet a the position of the screen"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet at (0 0)and then set current position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet value in a decimal value.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ Move the bullet up the screen"""
        # update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect factor.
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
