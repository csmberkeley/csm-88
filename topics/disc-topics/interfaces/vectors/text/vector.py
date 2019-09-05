class Vector:
    def __init__(self, vector):
        self.vector = vector

    def __neg__ (self)       : "*** YOUR CODE HERE ***"
    def __add__ (self, other): "*** YOUR CODE HERE ***"
    def __sub__ (self, other): return self.__add__(-other)
    def __mul__ (self, other): "*** YOUR CODE HERE ***"
    def __rmul__(self, other): return self.__mul__(other)
    def __len__(self)        : return len(self.vector)
    def __getitem__(self, n) : return self.vector[n]
