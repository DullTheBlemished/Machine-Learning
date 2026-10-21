from random import uniform as rand
class linearRegression():
    def __init__(self, learning_rate):
        self.weight = rand(0, 2)
        self.N = 0
        self.total_loss = 0
        self.learning_rate = learning_rate

    def lossFunction(self, area, cost):
        self.N += 1
        guess = self.weight * area
        self.total_loss += (guess - cost)**2

        return 2 * area * (guess - cost)
    
    def learn(self, area, cost):
        try:
            slope = self.lossFunction(area, cost)
            self.weight -= self.learning_rate * slope

        except:  # this was because my dataset generator was messed up
            return "0"
        return "1"
        
    def guess(self, area, cost):
        return self.weight * area
