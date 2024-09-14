import math

def find_square_root():
    # Ask the user for input
    num = float(input("Enter a number to find its square root: "))
    
    if num < 0:
        print("The square root of a negative number is a complex number.")
        return
    
    # Calculate the square root
    sqrt = math.sqrt(num)
    
    # Display the result
    print(f"The square root of {num} is {sqrt}")

# Run the function
find_square_root()
