import math

class Activation:
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.e ** x)

    @staticmethod
    def derivativeSigmoid(y):
        #return Activation.sigmoid(x) * (1 - Activation.sigmoid(x))
        return y * (1 - y) # y has already been 'sigmoided'