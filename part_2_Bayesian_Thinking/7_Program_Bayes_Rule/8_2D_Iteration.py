# 1. Create the world

import numpy as np

# A 6x5 robot world
world = np.array([ [0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 1, 0, 0],
                   [0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 0],
                   [1, 0, 0, 0, 0] ])

# Print out some information about the world
print(world)

print('\nThe shape of this array is: ' + str(world.shape))//



"" OUTPUT 

[[0 0 0 1 0]
 [0 0 0 1 0]
 [0 1 1 0 0]
 [0 0 0 0 1]
 [1 0 0 1 0]
 [1 0 0 0 0]]

The shape of this array is: (6, 5) ""
