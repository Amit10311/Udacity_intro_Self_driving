import numpy as np

# A 1x7 road
road = np.array(['r', 'r', 'r', 'r', 'r', 's', 'r'])

# Iterate through the array
length = len(road)
for index in range(0, length):
    
    # Find and store the value at each index
    value = road[index]
    # Print a new line and the value
    print('road['+str(index)+'] = '+str(value))
    
    
"" OUTPUT ""

"" road[0] = r
road[1] = r
road[2] = r
road[3] = r
road[4] = r
road[5] = s
road[6] = r ""
