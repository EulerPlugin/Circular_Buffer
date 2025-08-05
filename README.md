# Circular_Buffer

A circular buffer is a data structure used to efficiently implement a delay line. In a typical array-based approach, inserting a new sample requires shifting all existing data, resulting in O(N) complexity. However, a circular buffer only updates pointers, achieving O(1) performance.


Circular buffer를 구현하는 방식에는 몇 가지가 있다. 대표적으로 write pointer가 버퍼 크기를 넘을 경우를 처리하는 wraparound 방식에는 다음과 같은 코드들이 있다:

write_pointer = write_pointer + 1
if write_pointer >= buffer_size:
    write_pointer -= buffer_size
write_pointer = write_pointer + 1
if write_pointer == buffer_size:
    write_pointer -= buffer_size
write_pointer = (write_pointer + 1) % buffer_size
이 강의에서는 비트 마스크를 활용한 Wraparound Optimization 방식을 사용했다. 이 방식은 버퍼 크기가 2의 거듭제곱일 때만 사용 가능하며, 다음과 같이 wrap mask를 계산한다:
wrap_mask = buffer_size - 1
write_pointer = (write_pointer + 1) & wrap_mask
이를 위해 먼저 사용자가 요청한 버퍼 크기보다 크거나 같은 2의 거듭제곱값을 찾아야 한다. 이 연산은 다음과 같은 수식으로 정의된다:
clp2(x) = 2^ceil(log2(x))
wrap mask는 이 값을 기반으로 clp2(x) - 1로 정의된다. 예를 들어, x = 5라면 clp2(5) = 8, 따라서 wrap_mask = 7이 된다.
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
