def probability_range_improved(low_range, high_range, minimum, maximum):

    # TODO: calulate and return the probability 
    # even if low range is greater than high range.
    # Use the abs() function or if statements
    if low_range > high_range : 
      probability = abs(high_range -low_range)/(maximum-minimum )
    else: 
      probability = (high_range -low_range)/(maximum-minimum )

    return probability
    
    
    
## TODO: Test your results by running this cell.

assert "{0:.2f}".format(probability_range_improved(25, 700, 5, 800)) == '0.85'
assert "{0:.2f}".format(probability_range_improved(700, 25, 5, 800)) == '0.85'
print('Nice work!')
