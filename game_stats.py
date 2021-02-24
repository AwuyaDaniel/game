class GameStats():

    """Tracking statistics for alien invasion"""
    def __init__(self, ai_settings):
        """Initializing statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start alien invasion in an active state
        self.game_active = True

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Initializing statistics thta can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        