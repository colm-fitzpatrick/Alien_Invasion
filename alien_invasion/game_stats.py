class GameStats:
    ''' Track statistics for Alien Invasion '''

    def __init__(self, ai_game):
        ''' Initialise statistics '''
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state
        self.game_active = False

        # High score should never be reset
        try:
            with open("highscore.txt","r") as hs:
                self.high_score = int(hs.read())
        except:
            self.high_score = 0

    def reset_stats(self):
        ''' Initialise statistics that can change during the game '''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
