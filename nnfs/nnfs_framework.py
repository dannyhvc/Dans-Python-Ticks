import numpy as np
import nnfs
from abc import ABC, abstractmethod
from nnfs.datasets import spiral_data
import matplotlib.pyplot as plt

nnfs.init()


class Layer_Dense:
    def __init__(self, n_inputs: int, n_neurons: int):
        self.weights = .1 * np.random.randn(n_inputs, n_neurons)
        self.bias = np.zeros(shape=(1, n_neurons))

    def forward(self, inputs: np.ndarray):
        self.output = (inputs @ self.weights) + self.bias


class Activation_ReLU:
    def forward(self, inputs: np.ndarray) -> np.ndarray:
        self.output = np.maximum(0, inputs)


class Activation_Softmax:
    def forward(self, inputs: np.ndarray) -> np.ndarray:
        exp_val = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        self.output = exp_val / np.sum(exp_val,  axis=1, keepdims=True)

    # Backward pass
    def backward(self, dvalues):
        # Create uninitialized array
        self.dinputs = np.empty_like(dvalues)
        # Enumerate outputs and gradients
        for index, (single_output, single_dvalues) in \
                enumerate(zip(self.output, dvalues)):
            # Flatten output array
            single_output = single_output.reshape(-1, 1)
            # Calculate Jacobian matrix of the output
            jacobian_matrix = np.diagflat(single_output) - \
            np.dot(single_output, single_output.T)
            # Calculate sample-wise gradient
            # and add it to the array of sample gradients
            self.dinputs[index] = np.dot(jacobian_matrix,
            single_dvalues)


class Loss(ABC):
    def calculate(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        sample_losses = self.forward(y_true, y_pred)
        data_loss = np.mean(sample_losses)
        return data_loss

    @abstractmethod
    def forward(self,
                y_pred: np.ndarray,
                y_true: np.ndarray) -> np.ndarray: ...


class Loss_CategoricalCrossentropy(Loss):
    def forward(self, y_pred: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-10, 1.0 - 1e-10)

        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)
        return -np.log(correct_confidences)

    # Backward pass
    def backward(self, dvalues, y_true):
        # Number of samples
        samples = len(dvalues)
        # Number of labels in every sample
        # We'll use the first sample to count them
        labels = len(dvalues[0])
        # If labels are sparse, turn them into one-hot vector
        if len(y_true.shape) == 1:
            y_true = np.eye(labels)[y_true]
        # Calculate gradient
        self.dinputs = -y_true / dvalues
        # Normalize gradient
        self.dinputs = self.dinputs / samples


def test_nnfs():
    X, y = spiral_data(samples=100, classes=3)
    # decl
    dense1 = Layer_Dense(2, 3)
    act1 = Activation_ReLU()
    dense2 = Layer_Dense(3, 3)
    act2 = Activation_Softmax()
    # forward
    dense1.forward(X)
    act1.forward(dense1.output)
    dense2.forward(act1.output)
    act2.forward(dense2.output)
    # loss
    loss = Loss_CategoricalCrossentropy()
    loss = loss.calculate(act2.output, y)
    print(f"loss = {loss}")
    print(
        f"""
        weights: \n{dense1.weights},
        shape: {dense1.weights.shape}
        """
    )

    # plotting
    figure = plt.figure()
    ax1: plt.Axes = figure.add_axes(rect=[0.1, 0.1, 0.8, 0.8])
    ax1.scatter(
        x = range(dense1.weights.shape[1] * dense1.weights.shape[0]) ,
        y = dense1.weights,
        c="red"
    )
    ax1.scatter(
        x = range(dense2.weights.shape[1] * dense2.weights.shape[0]) ,
        y = dense2.weights,
        c="orange"
    )
    plt.show()

    # from matplotlib.animation import FuncAnimation

    # fig, ax = plt.subplots()
    # xdata, ydata = [], []
    # ln, = plt.plot([], [], 'ro')

    # def init():
    #     ax.set_xlim(0, 2*np.pi)
    #     ax.set_ylim(-1, 1)
    #     return ln,

    # def update(frame):
    #     xdata.append(frame)
    #     ydata.append(np.sin(frame))
    #     ln.set_data(xdata, ydata)
    #     return ln,

    # ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
    #                     init_func=init, blit=True)

    plt.show()




def main():
    test_nnfs()


if __name__ == '__main__':
    main()
