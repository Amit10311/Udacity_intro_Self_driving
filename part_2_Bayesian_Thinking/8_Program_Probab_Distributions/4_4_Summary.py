def probability_range_improved(low_range, high_range, minimum, maximum):

    # TODO 1: check if any of the inputs are strings.
    # hint: the python function isinstance() will be useful
    
    if (isinstance(low_range, str) or isinstance(high_range, str)):
        print('Inputs should be numbers not string \n')
        return None
    
    # TODO 2:  check that low_range is between minimum and maximum
    if (minimum > low_range or low_range > maximum):
        print('Your low range value must be between minimum and maximum \n')
        return None
        
    # TODO 3: check that high_range is between min and max
    if (minimum > high_range or high_range > maximum):
        print('The high range value must be between minimum and maximum \n')
        return None

    # TODO 4: calulate and return the probability 
    # even if low range is greater than high range
    else: 
        probability = abs(high_range -low_range)/(maximum-minimum)
    return probability
    
    
    
    
## TODO: Test your results by running this cell. 

assert probability_range_improved('a', 0, -100, 500) == None
assert probability_range_improved(0, 'b', -100, 500) == None
assert probability_range_improved(-100, 300, 100, 500) == None
assert probability_range_improved(105, 700, 100, 500) == None
assert "{0:.2f}".format(probability_range_improved(25, 700, 5, 800)) == '0.85'
assert "{0:.2f}".format(probability_range_improved(700, 25, 5, 800)) == '0.85'
print('You got the results we were looking for!')
