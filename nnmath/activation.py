import math

class Activation:
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.e ** x)