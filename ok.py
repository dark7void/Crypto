import math
import sys
import os
import time #remove

def _rotate_right(num: int, shift: int, size: int = 32):
    """Rotate an integer right."""
    return (num >> shift) | (num << size - shift)
    
def f(num: int):
    """As defined in the specification."""
    num = (_rotate_right(num, 7) ^
           _rotate_right(num, 18) ^
           (num >> 3))
    return num

sys.set_int_max_str_digits(1000000000)

init = ' '.join(sys.argv[1:])
    
d_array = []
for i in init:
    #_print(i, end="")

    d_array.append(ord(i))

#_print()
d=d_array[0]

l=""
for i in d_array:
    sq2 = format(math.sqrt(2)*i, '.49f')
    sq2 = str(sq2)[str(sq2).find(".")+1:]
    l = l + sq2

#_print(l)
n = len(l) // 4
a = int(l[:n])
b = int(l[n:2*n])
c = int(l[2*n:3*n])
d = int(l[3*n:])

#_print(f"a = {a}")
#_print(f"b = {b}")
#_print(f"c = {c}")
#_print(f"d = {d}")

#_os.system('clear')
n = 0
for i in range(16):
    #_os.system('clear')
    a = b 
    b = c 
    c = d % 2**32
    d = f(a ^ f(b))
    #_print("~")
    #_print("a: " + str(a))
    #_print("b: " + str(b))
    #_print("c: " + str(c))
    #_print("d: " + str(d))
    #_time.sleep(0.3)
    n += 1
    #_print(n)
    
final = str(a) +str(b) +str(c) +str(d) 
#_print(final)

print(hex(int(final)))
#_print(len(hex(int(final))))
