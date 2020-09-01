class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60 #这样直接就是tuple
        self.bullet_allowed = 3

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        self.fleet_direction = 1

        self.speedup_scale = 1.1

        self.alien_points = 50

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1

    def increased_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale


        