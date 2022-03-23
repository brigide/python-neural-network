import matplotlib.pyplot as plt
import matplotlib.animation
from random import uniform

from perceptron import Perceptron 
from trainer import Trainer

def f(x):
    return x

def main():
    #coordinate space
    xmin = 0
    ymin = 0
    xmax = 640
    ymax = 360

    count = 0 #count of points training
    bias = 1 #bias value
    trainingPoints = 1 #amount of training points

    #we get three inputs for x, y and bias
    perceptron = Perceptron(3, 0.0001) #low learning rate b/c of visual, not optimal

    #creates a random set of training points
    training = []
    for i in range(trainingPoints):
        x = uniform(xmin, xmax)
        y = uniform(ymin, ymax)
        answer = 1
        if (y < f(x)):
            answer = -1
        training.append(Trainer(x, y, bias, answer))
        print(training[i].toString())

    print('first guess')
    guess = perceptron.feedFoward(training[0].inputs)
    print('guess: ' + str(guess))
    print('desired: ' + str(training[0].answer))
    print('weights: ' + str(perceptron.getWeights()))

    while guess != training[0].answer:
        #Train the Perceptron with one "training" point at a time
        perceptron.train(training[0].inputs, training[0].answer)
        count = (count + 1) % len(training)


        print('\ntraining...')
        guess = perceptron.feedFoward(training[0].inputs)
        print('guess: ' + str(guess))
        print('desired: ' + str(training[0].answer))
        print('weights: ' + str(perceptron.getWeights()))

if __name__ == '__main__':
    main()