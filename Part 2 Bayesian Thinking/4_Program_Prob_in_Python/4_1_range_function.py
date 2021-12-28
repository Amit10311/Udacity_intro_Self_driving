# -*- coding: utf-8 -*-

# This is an example of a nested loop
# Nested loops are loops inside of loops
# the left_num will increment slower than the right_num

# How many times will right_num perform full loops? 25 times 

for left_num in range(3):
    for right_num in range(4):
        product = left_num * right_num
        print(left_num, "x", right_num, "=", product)
        
"""Return a float
0 x 0 = 0
0 x 1 = 0
0 x 2 = 0
0 x 3 = 0
1 x 0 = 0
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 0 = 0
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
"""
