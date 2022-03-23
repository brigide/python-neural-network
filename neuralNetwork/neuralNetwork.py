from numpy import gradient
from nnmath.matrix import Matrix
from nnmath.activation import Activation

class NeuralNetwork:
    def __init__(self, inputs, hidden, outputs, learningRate):
        self.input_nodes = inputs
        self.hidden_nodes = hidden
        self.output_nodes = outputs
        self.learningRate = learningRate

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


    def train(self, inputs, targets):
        #converts simple array into Matrix object
        inputs = Matrix.fromArray(inputs)
        #make a guess

        # uses matricial multiplication in order to get the sum of weights and inputs for each hidden layer
        hidden = Matrix.multiply(self.weights_ih, inputs)

        hidden.add(self.bias_h) # add bias values element-wise for each hidden node value

        # hidden activation function
        hidden.map(Activation.sigmoid)

        # repeating process for output
        outputs = Matrix.multiply(self.weights_ho, hidden)
        outputs.add(self.bias_o)

        outputs.map(Activation.sigmoid)



        #train

        #convert array to Matrix object
        targets = Matrix.fromArray(targets)


        # calculation of the error
        # error = targets - outputs
        output_errors = Matrix.subtract(targets, outputs)

        #calculating deltas = learning rate * errors matrix * derivative sigmoid of each output * transposed sigmoided inputs
        #get the sigmoid derivative for each output
        #calculating the gradient
        gradients = Matrix.newMap(outputs, Activation.derivativeSigmoid) # transform all sigmoided outputs in it's derivative 
        gradients.multiplyHamard(output_errors) # multiply the result by the output error
        gradients.multiplyScalar(self.learningRate) # multiply the result by the learning rate

        #calculating the deltas
        hidden_t = Matrix.transpose(hidden) # transpose sigmoided inputs
        weights_ho_deltas = Matrix.multiply(gradients, hidden_t) # multiplying the result gradients by the trasnposed hidden layer
        #apply the found deltas adjustment in the current weights
        self.weights_ho.add(weights_ho_deltas)


        # repeat the process for the input->hidden weights (ih)
        weights_ho_t = Matrix.transpose(self.weights_ho) # transpose the weight's matrix from hidden to output
        hidden_errors = Matrix.multiply(weights_ho_t, output_errors) # multiply transposet weights by the previously calculated errors

        #calculating gradients
        hidden_gradients = Matrix.newMap(hidden, Activation.derivativeSigmoid)
        hidden_gradients.multiplyHamard(hidden_errors)
        hidden_gradients.multiplyScalar(self.learningRate)

        #calculating deltas
        inputs_t = Matrix.transpose(inputs)
        weights_ih_deltas = Matrix.multiply(hidden_gradients, inputs_t)

        self.weights_ih.add(weights_ih_deltas)

        outputs.toTable()
        targets.toTable()
        output_errors.toTable()
        # hidden_errors.toTable()
        self.weights_ho.toTable()
        # self.weights_ih.toTable()

