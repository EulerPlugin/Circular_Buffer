import numpy as np

def next_power_of_2(x):
    return int(2 ** np.ceil(np.log2(x)))


class CircularBuffer:
    def __init__(self, size: int):
        size = next_power_of_2(size)
        self._wrap_mask = size - 1
        self._buffer = np.zeros((size, ))
        self._write_pointer = 0
    
    def write_sample(self, sample: float):
        self._buffer[self._write_pointer] = sample
        self._write_pointer = (self._write_pointer + 1) & self._wrap_mask
    
    def read_sample(self, delay: int):
        assert delay >= 1
        assert delay <= self._buffer.size - 1

        read_pointer = (self._write_pointer - delay) & self._wrap_mask
        print(self._buffer[read_pointer])
        return self._buffer[read_pointer]
        
circle = CircularBuffer(4)

circle.write_sample(1)
circle.write_sample(2)
circle.write_sample(3)
circle.write_sample(4)
circle.write_sample(5)

circle.read_sample(1)
circle.read_sample(2)
circle.read_sample(3)