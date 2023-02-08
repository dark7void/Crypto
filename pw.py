#!/bin/python
# generate a password with length of argv

import random
import string
import sys

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == '__main__':
    password_length = int(sys.argv[1])
    password = generate_password(password_length)
    print(password)
