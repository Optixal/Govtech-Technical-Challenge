#!/usr/bin/python3
# Shawn Pang

import string
from itertools import permutations

def main():
    for password in permutations(string.digits + string.ascii_letters, 16):
        password = ''.join(password)
        print(password)
        #test_password(password) # Uncomment if test_password is available
    
if __name__ == '__main__':
    main()
