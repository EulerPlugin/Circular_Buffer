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

Circular buffer에는 다음과 같은 두 가지 주요 구현 방식이 있다:

Variable Delay Circular Buffer
하나의 write pointer만 유지
읽을 때 delay를 직접 지정
read_sample(delay)에서 read_pointer = (write_pointer - delay) & wrap_mask 방식으로 읽기
delay 값을 매번 다르게 줄 수 있어 유연함
Fixed Delay Circular Buffer with Read Pointer
write pointer와 read pointer를 모두 유지
write와 read 수가 다르면 overrun 또는 underrun이 발생할 수 있음
실시간 처리에 적합 (고정된 딜레이, 일정한 읽기/쓰기 주기 유지 가능)
