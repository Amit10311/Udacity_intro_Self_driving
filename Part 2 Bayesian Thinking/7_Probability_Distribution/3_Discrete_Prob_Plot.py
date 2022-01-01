from matplotlib import pyplot as plt

# This line is needed
%matplotlib inline

def plot_probability(roll_data):
   
    roll_outcomes = [2,3,4,5,6,7,8,9,10,11,12]

    fig, ax = plt.subplots()
    ax.bar(roll_outcomes, roll_data)    # (x,y)

    ax.set_xlabel("Sum of Rolling Two Dice")
    ax.set_ylabel(" Probability")
    ax.set_title("Probability of the Sum when Rolling Two Dice")
    plt.show()
    
plot_probability(normalized_counts)
