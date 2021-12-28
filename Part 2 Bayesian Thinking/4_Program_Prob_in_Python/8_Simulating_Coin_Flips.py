# 1. Import the random module and reference it as rd
import random as rd

# 2. Things known 
num_trials = 100 # Sets the number of flips
heads = 0 # A counter for the number of heads
tails = 0 # A counter for the number of tails
p_heads = 0.5 # The probability for heads

# 3. Simulate coin flips up to the num_trials specified

for i in range(num_trials):
    # Collect a random number between [0,1]
    random_number = rd.random()
    # If the number is less than heads count it as heads
    # Otherwise, count it as tails
    if random_number < p_heads:
        heads = heads + 1
    else:
        tails += 1
        
print("Random number:", random_number,"\n")

print("In", num_trials, "trials there were", heads, "heads and", tails, "tails. \n")
print("PERCENT HEADS:", 100 * heads/num_trials, "percent \n")
print("PERCENT TAILS:", 100 * tails/num_trials, "percent")


## OUTPUT 

"""Random number: 0.5329357409498365 

# In 100 trials there were 42 heads and 58 tails. 

PERCENT HEADS: 42.0 percent 
PERCENT TAILS: 58.0 percent
"""
