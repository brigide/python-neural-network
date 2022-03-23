#simple perceptron class
class Perceptron:

    #consntructor class
    def __init__(self, n, learningRate):
        #initialize weights
        self.weights = []
        for i in range(n):
            self.weights.append(i)

        #initialize learning rate
        self.learningRate = learningRate


    #perceptron training function
    #weights are adjusted based on desired output
    def train(self, inputs, desired):
        #guess the result
        guess = self.feedFoward(inputs)

        #Compute the factor for changing the weight based on the error
        #Error = desired output - guessed output
        #Note this can only be 0, -2, or 2
        #Multiply by learning constant
        error = desired - guess

        #adjust weights based on weightChange * input
        for i in range(len(self.weights)):
            self.weights[i] += self.learningRate * error * inputs[i];         
        

    #function returns a guess
    def feedFoward(self, inputs):
        #sum all the inputs * it's weights
        sum = 0.0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weights[i]

        #returns the activation function, it's 1 or -1
        return self.activate(sum)

    #recieves the sum and clissifies it
    def activate(self, sum):
        if sum > 0:
            return 1
        return -1

    def getWeights(self):
        return self.weights
