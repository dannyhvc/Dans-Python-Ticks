import numpy as np
import math
import nnfs

nnfs.init()


def main():
    # batch
    layer_outputs = [[4.8, 1.21, 2.385],
                     [8.9, -1.81, .2],
                     [1.41, 1.051, .026]]

    # inputs -> { softmax: (exp -> normalization) } -> outputs
    exp_val = np.exp(layer_outputs)
    # print(np.sum(exp_val, axis=1, keepdims=True))
    norm_vals = exp_val / np.sum(exp_val, axis=1, keepdims=True)
    print(norm_vals)


if __name__ == '__main__':
    main()
