# The complement function takes in the probability of an event, P(A).
def complement(p_A):
    
    ## TODO: Change the value of complement
    ## So that it calculates the complement of any variable p_A
    complement = 1- p_A
    
    return complement

    
## TODO: Change this test value and test out your code!
p_test = 0.2

# Running your code with the p_test value
complement_test = complement(p_test)
print('Your function returned that the complement of '+str(p_test) +' is: '+str(complement_test))
