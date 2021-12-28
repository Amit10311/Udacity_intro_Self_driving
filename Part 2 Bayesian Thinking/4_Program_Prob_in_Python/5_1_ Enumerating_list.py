
# 1 Method 

print("Enumerating a list... \n")

my_list = [1, 2, 3, "a", "b", "c"]

for i, item in enumerate(my_list):
    print("item number", i, "is", item)
    
# 2 Method     
print("Another way to enumerate using a list 'method'... \n ")

for item in my_list:
    index = my_list.index(item)  
    print("item", item, "has index", index)

    
 ## OUTPUTS  
    
 """ Enumerating a list... 

item number 0 is 1
item number 1 is 2
item number 2 is 3
item number 3 is a
item number 4 is b
item number 5 is c """
