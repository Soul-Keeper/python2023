import numpy as np
import random

random.seed(0)
np.random.seed(0)


class My_Matrix(np.lib.mixins.NDArrayOperatorsMixin):
    def __init__(self, list):
        super().__init__()
        self.matrix = list
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    def __setitem__(self, index, value):
        self.matrix[index] = value

    def __getitem__(self, index):
        return self.matrix[index]

    def __str__(self):
        output = ''   
        for i in range(len(self.matrix)):
            output += ('|' + ''.join(map(lambda x:'{0:8.3f}'.format(x), self.matrix[i])) + '| \n')

        return output
    
    def __write__(self, filename):
        with open(filename, "w") as file:
            file.write(str(self.matrix))
    
    _HANDLED_TYPES = (list, int)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get("out", ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (My_Matrix,)):
                return NotImplemented
        inputs = tuple(
            x.matrix if isinstance(x, My_Matrix) else x for x in inputs
        )
        if out:
            kwargs["out"] = tuple(
                x.matrix if isinstance(x, My_Matrix) else x for x in out
            )
        result = getattr(ufunc, method)(*inputs, **kwargs)
        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == "at":
            return None
        else:
            return type(self)(result)


a = My_Matrix(np.random.randint(0, 10, (10, 10)))
b = My_Matrix(np.random.randint(0, 10, (10, 10)))

(a + b).__write__("artifacts/medium/matrix+.txt")
(a * b).__write__("artifacts/medium/matrix_mul.txt")
(a @ b).__write__("artifacts/medium/matrix@.txt")
