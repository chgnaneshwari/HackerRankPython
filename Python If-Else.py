#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2!= 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    # Case 2: If the number is even and in the range 2 to 5
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    # Case 3: If the number is even and in the range 6 to 20
    print("Weird")
elif n % 2 == 0 and n > 20:
    # Case 4: If the number is even and greater than 20
    print("Not Weird")
