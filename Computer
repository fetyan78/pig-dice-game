from random import shuffle

class Computer:
    def __init__(self, difficulty_level):
        if 0 < difficulty_level <4:
            self.difficulty_level=difficulty_level
        else:
            self.difficulty_level=1
        self.probability=self.set_probability()
        self.biased_list=self.generate_biased_list()
        self.decision_list=self.generate_decision_list()

    def get_difficulty_level(self):
            return self.get_difficulty_level
    
    def set_difficulty(self, difficulty_level):
            self.difficulty=difficulty_level

    def get_probability(self):
            return self.probability
        
    def generate_biased_list(self):
        biased_list=[]
        current_value=0
        for i in self.get_probability():
            i = i // 10
            current_value +=1
            for _ in range(i):
                biased_list.append(current_value)
        shuffle(biased_list)
        return biased_list
    
    def get_biased_list(self):
        return self.biased_list
    
    def generate_decision_list(self):
        match(self.get_difficulty()):
            case 1:
                decision_list = ["pass","pass","roll","roll","roll"]
                shuffle(decision_list)
                return decision_list
            case 2:
                decision_list = ["pass","roll","roll","roll","roll"]
                shuffle(decision_list)
                return decision_list
            case 3:
                decision_list = ["pass","roll","roll",
                                 "roll","roll","roll","roll"]
                shuffle(decision_list)
                return decision_list
            
    def get_decision_list(self):
        return self.decision_list
