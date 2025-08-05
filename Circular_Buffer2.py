'''
When the delay is fixed and we read and write the same number of samples in each iteration, 
maintaining a fixed processing order is often required.
In such cases, the circular buffer can be modified to include a read pointer.
'''

import numpy as np

def next_power_two(x):
    return int(2 ** np.ceil(np.log2(x)))

class CircularBuffer:
    def __init__(self, size: int, delay: int):
        size = next_power_two(size)
        self._wrap_mask = size - 1
        self._buffer = np.zeros((size, ))

        self._write_pointer = 0
        self._read_pointer = (self._write_pointer - delay) & self._wrap_mask

    def write_sample(self, sample: float):
        if self._write_pointer == self._read_pointer:
            raise Exception("Overrun: the write pointer passed the read pointer")
        
        self._buffer[self._write_pointer] = sample
        self._write_pointer = (self._write_pointer + 1) & self._wrap_mask

    def read_sample(self):
        if self._write_pointer == self._read_pointer:
            raise Exception("Underrun: the read pointer passed the write pointer")

        sample = self._buffer[self._read_pointer]
        self._read_pointer = (self._read_pointer + 1) & self._wrap_mask

        return sample

# Overrun example
cb = CircularBuffer(size=4, delay=2)
cb.write_sample(1)
cb.write_sample(2)
cb.write_sample(3)  # Overrun occurs here: write_pointer catches up to read_pointer


# Underrun example
cb = CircularBuffer(size=4, delay=4)  # delay == size → read_pointer == write_pointer
cb.read_sample()  # Underrun occurs here: trying to read before any write