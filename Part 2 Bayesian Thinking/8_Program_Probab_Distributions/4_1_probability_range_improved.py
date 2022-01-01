def probability_range_improved(low_range, high_range, minimum, maximum):

    # TODO: check if any of the inputs are strings.
    # hint: the python function isinstance() will be useful
    
    if (isinstance(low_range, str)):
        # print a message to the user and return none
        print('1. Inputs should be numbers not string')
        return None

    elif (isinstance(high_range, str)):
        # print a message to the user and return none
        print('2. Inputs should be numbers not string')
        return None

    else: 
      probability = abs(high_range -low_range)/(maximum-minimum )

    return probability
    
    
    
    
## TODO: Test your results by running this cell.
    
assert probability_range_improved('a', 0, -100, 500) == None
assert probability_range_improved(5, 'b', -100, 500) == None

assert "{0:.2f}".format(probability_range_improved(25, 700, 5, 800)) == '0.85'
assert "{0:.2f}".format(probability_range_improved(700, 25, 5, 800)) == '0.85'

print('Well done!')
