import math
import sys
import os
import time #remove

def _rotate_right(num: int, shift: int, size: int = 32):
    return (num >> shift) | (num << size - shift)
    
def f(num: int):
    num = (_rotate_right(num, 7) ^
           _rotate_right(num, 18) ^
           (num >> 3))
    return num

sys.set_int_max_str_digits(100000)

init = ' '.join(sys.argv[1:])
    
d_array = []
for i in init:
    print(i, end="")

    d_array.append(ord(i))

print()
d=d_array[0]

l=""
for i in d_array:
    sq2 = format(math.sqrt(2)*i, '.49f')
    sq2 = str(sq2)[str(sq2).find(".")+1:]
    l = l + sq2

print(l)
n = len(l) // 4
a = int(l[:n])
b = int(l[n:2*n])
c = int(l[2*n:3*n])
d = int(l[3*n:])

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")

os.system('clear')
for i in range(30):
    os.system('clear')
    a = b 
    b = c % 2**32
    c = d 
    d = f(a ^ f(b))
    print("~")
    print("a: " + str(a))
    print("b: " + str(b))
    print("c: " + str(c))
    print("d: " + str(d))
    #time.sleep(0.1)

final = str(a) +str(b) +str(c) +str(d) 
print(final)

print(hex(int(final)))
