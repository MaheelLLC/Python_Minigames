class Settings():
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 50, 50)
        
        # Pea settings
        self.pea_color = 255, 255, 0
        self.pea_width = 9
        self.pea_height = 5
        self.peas_allowed = 3

        # Rectangle settings
        self.rect_width = 100
        self.rect_height = 150
        self.rect_color = 255, 50, 50
        self.rect_direction = 1
        self.rect_speed_factor = 0.5
        
        # Lives
        self.lives = 3

        # Changing Difficulty
        self.speedup_scale = 1.1

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 0.75
        self.pea_speed_factor = 3
        self.rect_speed_factor = 0.5
        # Note that if you don't want changing difficulty, just return these
        # attributes to init and delete this method
        # Actually just change the speedup_scale to 1
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.pea_speed_factor *= self.speedup_scale
        self.rect_speed_factor *= self.speedup_scale