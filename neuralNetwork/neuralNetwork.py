from nnmath.matrix import Matrix
from nnmath.activation import Activation

class NeuralNetwork:
    def __init__(self, inputs, hidden, outputs):
        self.input_nodes = inputs
        self.hidden_nodes = hidden
        self.output_nodes = outputs

        # weights between inputs (i) and hidden (h)
        rows = self.hidden_nodes # one matrix row for each hidden node
        cols = self.input_nodes # one matrix column for each input node
        self.weights_ih = Matrix(rows, cols)
        self.weights_ih.randomize() # initialize weights with random values

        # weights between hidde (h) and output (o)
        rows = self.output_nodes # one matrix row for each output node
        cols = self.hidden_nodes # one matrix column for each hidden node
        self.weights_ho = Matrix(rows, cols)
        self.weights_ho.randomize() # initialize weights with random values

        #defines bias for hidden layer
        self.bias_h = Matrix(self.hidden_nodes, 1) # creates bias matrix based for each hidden node
        self.bias_h.randomize()

        #defines bias for output layer
        self.bias_o = Matrix(self.output_nodes, 1) # creates bias matrix based for each output node
        self.bias_o.randomize()



    def feedFoward(self, inputs_array):
        #converts simple array into Matrix object
        inputs = Matrix.fromArray(inputs_array)

        # uses matricial multiplication in order to get the sum of weights and inputs for each hidden layer
        hidden = Matrix.multiply(self.weights_ih, inputs)

        hidden.add(self.bias_h) # add bias values element-wise for each hidden node value

        # hidden activation function
        hidden.map(Activation.sigmoid)



        # repeating process for output
        output = Matrix.multiply(self.weights_ho, hidden)
        output.add(self.bias_o)

        output.map(Activation.sigmoid)

        return output.toArray()