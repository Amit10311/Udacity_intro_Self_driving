my_list = [1, 2, 3, "a", "b", "c"]

print("my_list is:", my_list)


# 2. Prints each element of a list individually   
print("Looping through a list...")
for item in my_list:
    print("item is", item)

    
# 3. Prints the number of elements in a list     
print("The len function is important!")

num_elements = len(my_list)
print("my_list has", num_elements, "elements \n")   
  
    
# 4. Using range to loop through a list by index
print("A less great way to loop through a list... \n")

for index in range(len(my_list)):
    item = my_list[index] # accessing an element in a list!   

    print("item is", item)
    

#### OUTPUT 

# my_list is: [1, 2, 3, 'a', 'b', 'c']

""" 2 OUTPUT 
Looping through a list...
item is 1
item is 2
item is 3
item is a
item is b
item is """

# 3 OUTPUT 
# The len function is important!
# my_list has 6 elements 


"""4 OUTPUT 
A less great way to loop through a list... 

item is 1
item is 2
item is 3
item is a
item is b
item is c
"""
