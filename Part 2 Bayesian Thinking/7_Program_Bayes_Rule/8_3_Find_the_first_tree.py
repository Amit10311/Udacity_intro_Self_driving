3. Find the first tree, 1, in the world
# This function is similar to our iterate2D function,
# But looks for the first tree in the array and prints its location [x][y]

def first_tree(world):
    # iterates through all indices starting at the top-left [0][0]
    for i in range(0, world.shape[0]):
        for j in range(0, world.shape[1]):

            # check if a tree is found
            if(world[i][j] == 1):
                # if so, print the index and leave the loop with a return statement
                print('First tree found at location: ['+str(i)+']['+str(j)+']')
                return 

            
# Call the first_tree function

first_tree(world)
First tree found at location: [0][3]
