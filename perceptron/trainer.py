class Trainer:
    def __init__(self, x, y, bias, answer):
        self.inputs = [x, y, bias]
        self.answer = answer

    def toString(self):
        return 'inputs: [' + str(self.inputs[0]) + ', ' + str(self.inputs[1]) + ']\nanswer: ' + str(self.answer) + '\n'