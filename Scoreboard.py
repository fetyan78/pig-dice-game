class Scoreboard: 
    def __init__(self, players_list):
        self.maximum_score = 100 
        self.wining_player = None 
        self.player_scores = []
        for player in players_list: 
            self.player_scores.append([player,0])
    
    def update_score(self, name, score):
        for i, player_score in enumerate(self.player_scores): 
            if name == player_score [0]:
                self.player_scores[i][1] += score 
    
    def update_name(self, current_name, new_name):
        for i, player_score in enumerate(self.player_scores):
            if current_name == player_score[0]: 
                self.player_scores[i][0] = new_name
    
    def resert_score(self, name):
        for i, player_score in enumerate(self.player_scores):
            if name == player_score[0]:
                self.player_scores[i][1] = 0 
                
    