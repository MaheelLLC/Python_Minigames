class GameStats():
    """Track stats for catch"""

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = True
        # When you want to add AI to this game, just change this value to True
        # instead of False.
    
    def reset_stats(self):
        self.lives_left = self.settings.lives_left