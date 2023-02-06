import time

a=100000
b=7

for i in range(1,100):
     print("-----------------")
     print("a: " + str(a))
     print("b: " + str(b))
     print((a**b)%(a**(b+1)))
     print("~~~~~")
     final = str((a**b)%(a**(b+1)))[len(str(a))+15:]
     print(final)
     print(hex(final))
     time.sleep(0.05)
     a = a + 1
