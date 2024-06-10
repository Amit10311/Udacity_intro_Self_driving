# This function uses nested for loops and knowledge
# about the shape of the array to print out each item with it's index

def iterate2D(world):
    # y-dimension (rows)
    for i in range(0, world.shape[0]):

        # x-dimension (columns)
        for j in range(0, world.shape[1]):
            print('Index ['+str(i)+']['+str(j)+'] = ' +str(world[i][j]))
            
            

# Call the iterate function
iterate2D(world)



"" OUTPUT 
Index [0][0] = 0
Index [0][1] = 0
Index [0][2] = 0
Index [0][3] = 1
Index [0][4] = 0
Index [1][0] = 0
Index [1][1] = 0
Index [1][2] = 0
Index [1][3] = 1
Index [1][4] = 0
Index [2][0] = 0
Index [2][1] = 1
Index [2][2] = 1
Index [2][3] = 0
Index [2][4] = 0
Index [3][0] = 0
Index [3][1] = 0
Index [3][2] = 0
Index [3][3] = 0
Index [3][4] = 1
Index [4][0] = 1
Index [4][1] = 0
Index [4][2] = 0
Index [4][3] = 1
Index [4][4] = 0
Index [5][0] = 1
Index [5][1] = 0
Index [5][2] = 0
Index [5][3] = 0
Index [5][4] = 0 ""
