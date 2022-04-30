#Part One
#Creating a Function
def sum_function(x, y, z):
    """This function returns the sume of three numbers."""
    return x + y + z

def product_function(x, y, z):
    """This function returns the product of three numbers."""
    return x * y * z

def average_function(x, y, z):
    """This function returns the average of three numbers."""
    return (x + y + z)/3

#Printing results
print(sum_function(1,2,3))
print(product_function(1, 2, 3))
print(average_function(1, 2, 3))


#Part Two
#Create Three Lambda Functions
add_numbers = lambda x, y, z: x + y + z
multiply_numbers = lambda x, y, z: x * y * z
average_numbers = lambda x, y, z: (x + y + z)/3

#Print Lambda Functions
print(add_numbers(1, 2 ,3))
print(multiply_numbers(1, 2, 3))
print(average_numbers(1, 2, 3))


#Part Three
#Create Lists 
list_one = [4, 6, 88, 24]
list_two = [17, 34, 9, 5]
list_three = [63, 20, 98, 4]

#Create Lambda Function
average_maker = lambda x, y, z: (x + y + z)/3

#Using Map
map_results = map(average_maker, list_one, list_two, list_three)
print(list(map_results))
