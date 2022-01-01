# This function takes in the road and determines where to stop
def find_stop_index(road):   
    stop_index = 0 
    
    # 1 TODO: Iterate through the road array
    length = len(road) 
    for index in range(0,length):
        value = road[index]
      
       # 2  TODO: Check if a stop sign ('s') is found in the array
        print(str(value))
        if value == 's':
            print('We\'ve reached the middle of the road and we\'re leaving the loop!')

            ## 4 and return the value of the index that is *right before* the stop sign
            stop_index = index-1
            
            ## 3 If one is, break out of your iteration
            break

    return stop_index
