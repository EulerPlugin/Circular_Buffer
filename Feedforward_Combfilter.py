import Circular_Buffer2 as cb
import numpy as np

M = 5
b_0 = 0.5
b_M = 0.5

delay_line = cb.CircularBuffer(size = M, delay = M)

def FFCF(x):
    y = np.zeros_like(x)

    for i in range(len(x)):
        delayed_sample = delay_line.read_sample()
        delay_line.write_sample(x[i])

        y[i] = x[i] * b_0 + delayed_sample * b_M

    return y

        