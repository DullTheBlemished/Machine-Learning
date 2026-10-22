from random import uniform as rand

class linearRegression2D():
    def __init__(self, weight_learning_rate, weight = rand(0, 2), bias = rand(100000, 300000), test_cases=0):
        self.weight = weight # x
        self.bias = bias # c
        self.N = 0
        self.total_loss = 0
        self.weight_learning_rate = weight_learning_rate
        self.bias_learning_rate = 0.5
        self.test_cases = test_cases

    def lossFunction(self, area, cost):
        self.N += 1
        guess = self.weight * area + self.bias
        self.total_loss += (guess - cost)**2
        thingy = 2 * (self.weight*area + self.bias - cost)

        return (thingy * area, thingy)
    
    def learn(self, area, cost):  
        try:
            slopes = self.lossFunction(area, cost)
            weight_slope = slopes[0]
            bias_slope = slopes[1]

            self.weight -= self.weight_learning_rate * weight_slope
            self.bias -= self.bias_learning_rate * bias_slope

        except:
            return "0"
        self.test_cases += 1
        return "1"
        
    def guess(self, area, cost):
        guess = self.weight * area + self.bias
        error = max(guess, cost) - min(guess, cost)
        return (guess, error)

    def info(self):
        return (self.weight, self.bias, self.test_cases)
