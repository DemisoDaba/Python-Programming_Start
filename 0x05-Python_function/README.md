# Begin by using the def keyword to define the function
# Inside the parentheses after the function name, 
# specify the parameters the function expects. 
# In this case, we need two parameters: a and b, 
# representing the numbers to be added.

# After the colon :, 
# indent the code block that makes up the body of the function. 
# This is where you'll write the instructions 
# for adding the numbers.

# Congrats! You have successfully defined the function. 
# You can now use it in your code. 
# To call the function and retrieve the result, 
# use its name followed by parentheses, passing the required arguments.

def sum_two_numbers(a,b): # Begin by using the def keyword to define the function
    sum = a+b
    return sum


result = sum_two_numbers(3, 5)
print(result)

# Putting it all together, here's the complete code:

def sum_two_numbers(a,b):
    sum = a+b
    return sum
result = sum_two_numbers(3, 5)
print(result)  
