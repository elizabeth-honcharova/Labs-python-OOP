"""

    Task 4

    Program solves the knapsack problem

"""

from argparse import ArgumentParser

if __name__ == "__main__":
    
    parser = ArgumentParser()
    # the 1-st arg is capacity (int) and the others are weights (float)
    parser.add_argument("capacity", type = int)
    parser.add_argument("weights", type = float, nargs = "+")
    arg = parser.parse_args()

    nbars = len(arg.weights)

    def max_weight(nbars, weight_limit):
        """
        Counts max weight of bars (type = float) 
        with current weight of the bar, number of bars and capacity
        """

        # if there are no bars, 
        # then the max weight is zero

        if nbars == 0:  
            return 0  

        # if the weight of the bar is greater than the allowed weight, 
        # then the result is equal to the max weight without this bar

        elif arg.weights[nbars - 1] > weight_limit:
            return max_weight(nbars - 1, weight_limit)  
        
        # else return max of cases 
        # (the one excludes and the other includes the current bar)

        else:
            return max(max_weight(nbars - 1, weight_limit),  
                    max_weight(nbars - 1, weight_limit - arg.weights[nbars - 1])
                    + arg.weights[nbars - 1])  

    result = []
    weight_limit = arg.capacity

    # start with the allowed weight = full capacity and all nbars
    for i in reversed(range(nbars)):

        # if the highest value with all available bars (until highest index) 
        # is greater than the value without the current bar (with the highest index)
        # then add the current bar to the result 

        if max_weight(i + 1, weight_limit) > max_weight(i, weight_limit):
            result.append(arg.weights[i])  
            weight_limit -= arg.weights[i]

    print("Maximum weight of gold:", sum(result))