# Python function to divide 2 numbers
def divisionFunction (numerator, denominator):
    result = None
    try:
        result = numerator/denominator
    except ZeroDivisionError:
        print (f"Unable to divide by zero! You specified: {numerator}/{denominator}")
    
    # What else could go potentionally wrong here?

    print (f"{numerator}/{denominator} = {result}")
    return result

############################## MAIN application code ######################
# Perform some calculations with division
###########################################################################
divisionFunction(100,5)
divisionFunction(9,3)
divisionFunction(1,0)  #Ops!
divisionFunction(1000,0.25) 

# How could I prompt the user to choose to either add, subtract, divide , multiple just 2 numbers?