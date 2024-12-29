import numpy as np

#Define the precptron class
class Preceptron:
    def _init_ (self, input_size, lr=0.1):
        self.W = np.zeros(input_size + 1)
        self.lr = lr
    def activation_fn(self, x):
        return 1 if x >=0 else 0
    def predict (self, x):
        x = np.insert(x, 0 ,1)
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        return a
    def train(self, X, Y, epochs):
        for _ in range (epochs):
            for i in range(Y.shape[0]):
                  x = X[i]
                  y = self.predict(x)
                  e = Y[i] -y
                  self.W = self.W + self.lr * e * np.insert(x, 0, 1)

# Define the input data and labels

X = np.array([
    [0,0,0,0,0,0,1,0,0,0], #0
    [0,0,0,0,0,0,0,1,0,0], #1
    [0,0,0,0,0,0,0,0,1,0], #2
    [0,0,0,0,0,0,0,0,0,1], #3

])

            
            
                  
