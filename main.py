from neuralNetwork.neuralNetwork import NeuralNetwork

def main():
    nn = NeuralNetwork(2, 2, 2, 0.1)

    inputs = [1, 0]
    targets = [1, 0]

    #output = nn.feedFoward(inputs)
    nn.train(inputs, targets)
    #print(output)



if __name__ == '__main__':
    main()