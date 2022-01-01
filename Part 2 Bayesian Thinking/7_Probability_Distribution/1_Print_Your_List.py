#### 
# TODO: Create a Python list of the values in the 'Count' column.
# Your list should start with 54 and follow the same order
# as the data in the column: 54, 111, 163, etc.
###

count_data = [54,111,163,222,277,336,276,220,171,111,59]

# A for loop to print out every value in the count_data list
# The len() function determines the size of the list
# The range() function creates an integer 
#           list from 0 to len(count_data).

for i in range(len(count_data)):
   print(i+2,count_data[i])
