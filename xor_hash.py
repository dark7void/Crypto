# epic hashing algorythm based on rot and xors exclusively (HA!)
# 10/10 alan turing would recommend
#
# by dark7void

import math
import sys

def binary_to_hex(binary):
    hex_str = hex(int(binary, 2))[2:]
    return hex_str

def padding(s):
    while len(s) < 128:
        s += "0"
    return s
    
def rot(s, n):
    return s[n:] + s[:n]
    
def xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result
    
i = sys.argv[1]
print(i)

binary = ''.join(format(ord(x), 'b') for x in i)

binary = padding(binary)
print(binary)

#print(binary_to_hex(binary))

#print (binary)
rot7 = rot(binary, 7)
rot13 = rot(binary, 13)
#print(rot7)
#print(rot13)
xored = xor(rot7, rot13)
#print(xored)
rot7 = rot(rot13, 7)
rot13 = rot(rot13, 13)
xored = xor(rot7, rot13)
#print(xored)
rot7 = rot(rot13, 7)
rot23 = rot(rot13, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
old = rot7
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
xored = xor(xored, old)
#print(xored)
rot7 = rot(rot23, 7)
old = rot7
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
xored = xor(xored, old)
#print(xored)
rot7 = rot(rot23, 7)
old = rot7
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
rot7 = rot(rot23, 7)
rot23 = rot(rot23, 23)
xored = xor(xored, rot23)
#print(xored)
xored = xor(xored, old)
#print(xored)

print(binary_to_hex(xored)[:15])
