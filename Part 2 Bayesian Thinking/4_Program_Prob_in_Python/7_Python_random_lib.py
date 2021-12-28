# `random` is a Python "module".
# It provides functionality associated with randomness / probability. 

# what is happening when we write `import random as rd`,

import random as rd 

# 1. "Call the FUNCTION" named "random" and
# 2. assign the result of each "call to a variable"

a = rd.random()
b = rd.random()
c = rd.random()
print("a is", a)
print("b is", b)
print("c is", c)

# random isn't the only function in the random module.

print("\n Now keep pressing Ctrl+Enter to run this cell many times! \n")


# OUTPUT 
"""
a is 0.10238654130832847
b is 0.7437640456564217
c is 0.22159596793722303

Now keep pressing Ctrl+Enter to run this cell many times! 
"""

print (" choice([1, 2, 3, 5, 9]) : ", rd.choice([1, 2, 3, 5, 9]))
print (" \n choice('A String') : ", rd.choice('A String'))
