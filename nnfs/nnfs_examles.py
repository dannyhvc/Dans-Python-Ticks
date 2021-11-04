import numpy as np

class Layer_Dense(object):
    def __init__(self, n_inputs, n_neurons):
        self.weights = .1 * np.random.randn(n_inputs, n_neurons)
        self.bias = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = (inputs @ self.weights) + self.bias


def nnfs4_example():
    # list of multiple samples
    inputs: np.ndarray = np.array([
        [1, 2, 3, 2.5],
        [2, 5, -1, 2],
        [-1.5, 2.7, 3.3, -0.8],
    ])

    # starter weights
    weights: np.ndarray = np.array([
        [0.2, 0.8, -0.5, 1],
        [0.5, -0.91, 0.26, -.5],
        [-.26, -.27, .17, .87]
    ])
    # starter bias
    bias: np.ndarray = np.array([2, 3, .5])
    layer1_outputs: np.ndarray = (inputs @ weights.T) + bias
    print(layer1_outputs)

    # layer 2 weights
    weights2: np.ndarray = np.array([
        [0.1, -.14, 0.5],
        [-.5, .12, -.33],
        [-.44, .73, -.13]
    ])
    # layer 2 bias
    bias2: np.ndarray = np.array([-1, 2, -.5])
    layer2_outputs: np.ndarray = (layer1_outputs @ weights2.T) + bias2
    print(layer2_outputs)


def nnfs4_example_2():
    # list of multiple samples
    X: np.ndarray = np.array([
        [1, 2, 3, 2.5],
        [2, 5, -1, 2],
        [-1.5, 2.7, 3.3, -0.8],
    ])

    layer_1 = Layer_Dense(4, 5)
    layer_2 = Layer_Dense(5, 2)

    layer_1.forward(X)
    layer_2.forward(layer_1.output)
    print(layer_2.output)


def main():
    # nnfs4_example()
    nnfs4_example_2()


if __name__ == '__main__':
    main()
