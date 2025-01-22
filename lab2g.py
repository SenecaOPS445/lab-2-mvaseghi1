#!/usr/bin/env python3

# Author: Mohammad Vaseghi
# Author ID: 130349228
# Date Created: 2025/01/21

import sys

if len(sys.argv) != 1:
    timer =int(sys.argv[1])
else:
    timer = 3

while timer > 0 :
    print(timer)
    timer = timer -1 

print("blast off!")
