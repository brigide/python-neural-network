from neuralNetwork.neuralNetwork import NeuralNetwork

def main():
    nn = NeuralNetwork(2, 2, 1)

    inputs = [1, 0]

    output = nn.feedFoward(inputs)
    print(output)



if __name__ == '__main__':
    main()