# Matplotlib is one of the most common plotting packages in Python
# to use it more succinctly, you can call it   

from matplotlib import pyplot as plt

# This line is needed
%matplotlib inline

def visualize_one_die(roll_data):
    """
    Visualizes the dice rolls
    
    Args:
        roll_data (int): roll counts in a list from [1,6]
        
    Returns:
        None - shows a plot with the x-axis is the dice values
               and the y-axis as the frequency for t
    """

    roll_outcomes = [1,2,3,4,5,6]

    fig, ax = plt.subplots()
    ax.bar(roll_outcomes, roll_data)    # (x,y)

    ax.set_xlabel("Value on Die")
    ax.set_ylabel("# rolls")
    ax.set_title("Simulated Counts of Rolls")
    plt.show()
    
roll_data = simulate_dice_rolls(900)
visualize_one_die(roll_data)
