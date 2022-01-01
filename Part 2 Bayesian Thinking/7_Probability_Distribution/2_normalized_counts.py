###
# INSTRUCTIONS: Use a for loop to iterate through the 
#      count_data list
# 
# For each value in the list, divide the value by the total_count
# variable.
#
# You will need to append the results to a new list
#
###

normalized_counts = []

# TODO: Write a for loop to iterate through the count_data list.
#       Use the for loop example given previously to help
#       get yourself started

for i in range(len(count_data)):
    normalized_counts.append(count_data[i]/total_count)
    
    
    # TODO: Inside the for loop, divide each value in
    # count_data by the total_count variable and append
    # the result to the normalized_counts variable.

print('Here are the normalized counts: \n ' )
print(normalized_counts)
