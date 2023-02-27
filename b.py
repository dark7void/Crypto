import struct
import time
import os
import sys

sys.set_int_max_str_digits(1000000000)

def _rotate_right(num: int, shift: int, size: int = 32):
    return (num >> shift) | (num << size - shift)

def _sigma0(num: int):
    num = (_rotate_right(num, 7) ^
           _rotate_right(num, 18) ^
           (num >> 3))
    return num

message = "a" * 10009
for line in sys.stdin:
    message = message + line    

message = [ord(c) for c in message]
message = "".join([str(c) for c in message])
print(message)

message = message + "2"
    
while len(message) % 64 != 0:
    message = message + "1"

print(message)
segment_size = len(message) // 8

a = message[:segment_size]
b = message[segment_size:segment_size*2]
c = message[segment_size*2:segment_size*3]
d = message[segment_size*3:segment_size*4]
e = message[segment_size*4:segment_size*5]
f = message[segment_size*5:segment_size*6]
g = message[segment_size*6:segment_size*7]
h = message[segment_size*7:]

a, b, c, d, e, f, g, h = int(a), int(b), int(c), int(d), int(e), int(f), int(g), int(h)
for x in range(32):
    os.system('clear')
    temp = h

    h = g
    g = f 
    f = e 
    e = d ^ _sigma0(a ^ _sigma0(b ^ _sigma0(c ^ _sigma0(d ^ _sigma0(e ^ _sigma0(f)))))) % 2**32
    d = c
    c = b
    b = a

    a = temp % 2**32
    
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    time.sleep(1)
    
print(a, b, c, d, e, f, g, h)
final = str(a)[:6]+str(b)[:6]+str(c)[:6]+str(d)[:6]+str(e)[:6]+str(f)[:6]+str(g)[:6]+str(h)[:6]
print(final)
print(hex(int(final)))
