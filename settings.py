class Settings():
    """A class for storing all settings for alien invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # screen settings
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 1.2
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = (5, 5, 5)
        self.bullet_allowed = 5

        # Alien speed
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # Fleet direction of 1 represent right; -1 represent left
        self.fleet_direction = 1

        # How quickly the game speed up
        self.speedup_scale = 1.1

        # How quickly the alien point increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # Fleet direction of 1 represent right; -1 represent left
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed and alien score settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
