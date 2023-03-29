class Matrix:

    def __init__(self, list):
        self.matrix = list
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        
    def __getitem__(self, key):
        if isinstance(key, tuple):
            i = key[0]
            j = key[1]
            return self.matrix[i][j]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            i = key[0]
            j = key[1]
            self.matrix[i][j] = value

    def __str__(self):
        output = ''   
        for i in range(len(self.matrix)):
            output += ('|' + ''.join(map(lambda x:'{0:8.3f}'.format(x), self.matrix[i])) + '| \n')

        return output
    
    def __add__(self, other):
        res = Matrix([[0 for x in range(self.cols)] for y in range(self.rows)])

        if isinstance(other, Matrix):
            if (self.rows, self.cols) != (other.cols, other.rows):
                raise ValueError('Wrong size')

            for i in range(self.rows):
                for j in range(self.cols):
                    res.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

        elif isinstance(other, (int, float)):
            for i in range(self.rows):
                for j in range(self.cols):
                    res.matrix[i][j] = self.matrix[i][j] + other

        return res

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        res = Matrix([[0 for x in range(self.cols)] for y in range(self.rows)])

        #по-элементное перемножение
        if isinstance(other, Matrix):
            if (self.rows, self.cols) != (other.cols, other.rows):
                raise ValueError('Wrong size')

            for i in range(self.rows):
                for j in range(self.cols):
                    res.matrix[i][j] = self.matrix[i][j] * other.matrix[i][j]

        elif isinstance(other, (int, float)):
            for i in range(self.rows):
                for j in range(self.cols):
                    res.matrix[i][j] = self.matrix[i][j] * other
        
        return res

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __matmul__(self, other):
        if (self.rows != other.cols):
            raise ValueError('Wrong size')

        res = Matrix([[0 for x in range(self.rows)] for y in range(self.cols)])

        if isinstance(other, Matrix):
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.rows):
                        res.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return res
    
    
    
                    