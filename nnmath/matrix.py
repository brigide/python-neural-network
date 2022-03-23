from random import uniform, randint

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []

        for i in range(self.rows):
            self.data.append([])
            for j in range(self.cols):
                self.data[i].append(0)

    @staticmethod
    def fromArray(arr):
        m = Matrix(len(arr), 1)
        for i in range(len(arr)):
            m.data[i][0] = arr[i]

        return m

    def toArray(self):
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.data[i][j])
        return arr

    def toTable(self):
        print('-' * 60)
        for line in self.data:
            print('\t'.join(map(str, line)))
        print('-' * 60)


    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = uniform(-1, 1)

    @staticmethod
    def transpose(matrix):
        result = Matrix(matrix.cols, matrix.rows)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result.data[j][i] = matrix.data[i][j]
        return result

    def add(self, n):
        if type(n) == Matrix:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += n.data[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += n


    @staticmethod
    def subtract(a, b):
        # return a new matrix a - b
        result = Matrix(a.rows, a.cols)
        for i in range(a.rows):
            for j in range(a.cols):
                result.data[i][j] = a.data[i][j] - b.data[i][j]

        return result

    @staticmethod
    def multiply(a, b):
        # matrix product
        if a.cols != b.rows:
            print('columns of A must match rows of B')
            return
        
        result = Matrix(a.rows, b.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                # Dot product of values in col
                sum = 0
                for k in range(a.cols):
                    sum += a.data[i][k] * b.data[k][j]
                result.data[i][j] = sum
        
        return result


    def multiplyHamard(self, matrix):
        # hamard product
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= matrix.data[i][j]

    def multiplyScalar(self, n):
        # scalar product
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= n


    def map(self, fn):
        for i in range(self.rows):
            for j in range(self.cols):
                value = self.data[i][j]
                self.data[i][j] = fn(value)

    @staticmethod
    def newMap(matrix, fn):
        result = Matrix(matrix.rows, matrix.cols)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                value = matrix.data[i][j]
                result.data[i][j] = fn(value)
        return result