class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.lives_left = self.settings.lives