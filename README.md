# Circular_Buffer

A circular buffer is a data structure used to efficiently implement a delay line. In a typical array-based approach, inserting a new sample requires shifting all existing data, resulting in `O(N)` complexity. However, a circular buffer only updates pointers, achieving `O(1)` performance.

<p align="center">
  <img src="https://github.com/user-attachments/assets/06be3037-0430-43ce-b90b-997a4d5c5d09" width="183" height="688" />
</p>

<br>

### There are several ways to implement a circular buffer. 
One common aspect is how to handle the case when the write pointer exceeds the buffer size. Typical implementations include the following approaches:

~~~
write_pointer = write_pointer + 1

    if write_pointer >= buffer_size:
       write_pointer -= buffer_size
~~~

~~~
write_pointer = write_pointer + 1
    if write_pointer == buffer_size:
       write_pointer -= buffer_size
~~~

~~~
write_pointer = (write_pointer + 1) % buffer_size
~~~

<br>

### We used wraparound Optimization 

This project used a method based on bit masking. This approach is only applicable whten the buffer size is a power of two, and the wrap mask is calculated as follows:

~~~
wrap_mask = buffer_size - 1
write_pointer = (write_pointer + 1) & wrap_mask
~~~

To do this, we first need to find the smallest power of two that is greater than or equal to the buffer size requested by the user. This operation is defined by the following expression:

~~~
clp2(x) = 2^ceil(log2(x))
~~~

The wrap mask is then defined as `clp2(x) - 1`, based on this value. For example, if `x = 5`, then `clp2(5) = 8`, so the resulting `wrap_mask` is 7.

<p align="center">
<img width="207" height="76" alt="image" src="https://github.com/user-attachments/assets/b0c8887e-1803-465f-bbb0-a8955d5788ab" />
</p>

<p align="center">
<img width="437" height="159" alt="image" src="https://github.com/user-attachments/assets/2c7f2b91-5592-42a9-ad7e-d80b39a27b74" />
</p>

<br>

There are two main implementation approaches for circular buffers:

### Variable Delay Circular Buffer
- Only a write pointer is maintained
- The delay is specified directly at the time of reading
- Reading is done using `read_pointer = (write_pointer - delay) & wrap_mask`
- Allows flecibillity by supporting varying delay values for each read

### Fixed Delay Circular Buffer with Read Pointer
- Both write and read pointers are maintained
- If the number of writes and read differ, overrun or underrun may occur
- Suitable for real-time processing, where a fices delay and consistent read/write cycle are required

I devided my project into these tow implementation cases, and additionally worked on a 
__feedforward comb filter__ implementation using a circular buffer

<p align="center">
<img width="479" height="191" alt="image" src="https://github.com/user-attachments/assets/5174da67-ae88-4a1c-b59b-f374f3043bad" />
</p>


