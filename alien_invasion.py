import sys

import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from pygame.sprite import Group
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics and crate a scoreboard
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    # Make the play button
    play_button = Button(ai_settings, screen, "PLAY")

    # Make a ship   # Make a group to store bullets # Make a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # start the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        # redraw the screen during each pass through the screen
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        # make the most recent screen display
        pygame.display.flip()


run_game()
