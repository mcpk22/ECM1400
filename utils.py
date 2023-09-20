# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification


values = [1.1,100,99,2,5,7,7,10,10,10,-99,"hi"]





def check_type(values):
    '''
    Function recieves values in list 
    try if values in list is float(not non numerical)
    if yes return true
    if not return false
    
    Parameters:
        List:values
    Returns:
        true or false
     '''
    try:
        float(values)
        return True
    except:
        return False
 

def sumvalues(values):
    """
    Function recieves list and return the sum of all values
    Check if numbers in values is numerical

    Parameters:
        List:values
        count:sum starts at 0
    Returns:
        count:sum of all values
    """ 
    #Sum starts at 0 
    count=0
    for numbers in values:
        if check_type(numbers)== True:
            #if numbers checked in values are numerical
            count+=float(numbers)
    return count
        
#calling function
print("The Sum is ", sumvalues(values))


###############################################################

#insertion sort
def maxvalue(values):
    """
    Function recieves list of values and return the maximum value in the list

    check if the numbers in the list of values are numerical

    Parameters:
        List:values
        max:maximum in the list
        count: value of current number, used to loop for all values in list
    Returns:
        maximum value
    
    """    
    #new list for numerical numbers only
    new_values =[]
    
    for numbers in values:
        if check_type(numbers)== True:
            #if numbers checked in values are numerical
            new_values.append(numbers)
    
    count=0
    for count in range(len(new_values)):
        #go through all values
        max = new_values[0]
        for num in new_values:
            if num > max:
                max = num
                #if num is larger than max, num replace max 
                count= count+1
        return max


#callling funciton
print ("The Maximum value is", maxvalue(values))


##################################################################


def minvalue(values):
    """
    Function recieves list of values and return the minimum value in the list

    check if the numbers in the list of values are numerical

    Parameters:
        List:values
        min:minimum in the list
        count: value of current number, used to loop for all values in list
    Returns:
        minimum value
    
    """    
    #new list for numerical numbers only
    new_values =[]

    for numbers in values:
        if check_type(numbers)== True:
            #if numbers checked in values are numerical
            new_values.append(numbers)
    
    count=0
    
    for count in range(len(new_values)):
        #go through all values
        min = new_values[0]
        for num in new_values:
            if num < min:
                min = num
                #if num is smaller than max, num replace max 
                count= count+1
        return min

#calling function
print ("The Minimum value is", minvalue(values))


###############################################################


def meannvalue(values):
    """
    Function recieves list of values
    Check if the numbers in values are numerical
    Returns the mean of the list

    Parameters:
        List:values
    Returns:
        mean value
    """    
    #new list for numerical numbers only
    new_values =[]

    for numbers in values:
        if check_type(numbers)== True:
            #if numbers checked in values are numerical
            new_values.append(numbers)

    values = sumvalues(values)/len(new_values)
    return values
    

print ("The Mean of the values is ",round(meannvalue(values),3))


##############################################################


def countvalue(values,xw):
    """
    Funciton recieves list of values and variable
    Check if the numbers in values are numerical
    Returns the count of the list

    Parameters:
        List:values
        Variable:xw
    Returns:
        The value appeared the most in the list
    
    """    
    ## Your code goes here
    new_values =[]

    for numbers in values:
        if check_type(numbers)== True:
            #if numbers checked in values are numerical
            new_values.append(numbers)

    count = 0
    for i in range(len(new_values)):
        if new_values[i] == xw:
            count = count+1
    i = i+1
    return count
values = [1,1,1,12,3,4,5,"hi"]
print("The Count value is ", countvalue(values,1))