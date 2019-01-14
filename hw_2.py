from ctypes import c_long
from ctypes import pointer

ptr = pointer(c_long(0))
counter = 0

# Loop until forbidden memory segment
while True:
    ptr[counter] = 0
    counter += 1
    print(counter)
