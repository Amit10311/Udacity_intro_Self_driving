print("Enumerating a list... \n")

my_list = [1, 2, 3, "a", "b", "c"]

for i, item in enumerate(my_list):

    print("item number", i, "is", item)
    
    
print("Another way to enumerate using a list 'method'... \n ")

for item in my_list:
    index = my_list.index(item)
    
    print("item", item, "has index", index)
