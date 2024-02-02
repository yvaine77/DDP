"""
Factorial Calculator Function

Objective:
Write a function named 'calculate_factorial' to compute the factorial of a number using a for loop.

Function Parameter:
1. number (integer): A non-negative integer for which the factorial is to be calculated.

Instructions:
- Use a for loop to calculate the factorial of 'number'.
- Return the factorial result.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. calculate_factorial(5) should return the factorial of 5.
2. calculate_factorial(0) should return 1.
3. calculate_factorial(3) should return the factorial of 3.
4. calculate_factorial(-1) should handle negative input.
"""


def calculate_factorial(number):
    # Handle the edge case for negative inputs:
    if number < 0:
        return "Factorial is not defined for negative numbers."
    
    # Handle the edge case for 0:
    if number == 0:
        return 1

    # Initialize the factorial result
    factorial_result = 1

    # Calculate the factorial using a for loop:
    for i in range(1, number + 1): 
        factorial_result *= i  #this equals factorial_result = factorial_result * i
    """
    range 函数在 Python 中用来生成一个整数序列。range(start, stop) 会生成一个从 start 开始到 stop-1 结束的序列。
    在这个特定的情况下,range(1, number + 1) 生成了一个从1开始到 number 结束的序列。
    例如，如果 number 是5,那么 range(1, number + 1) 就会生成序列 [1, 2, 3, 4, 5]。
    之所以使用 number + 1 作为 range 的结束值，是因为 range 会包含开始值，但不包含结束值。
    为了确保序列包含 number,我们需要将结束值设置为 number + 1。
    """

    # Return the factorial result
    return factorial_result



# Test cases
print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(0))  # Expected output: 1
print(calculate_factorial(3))  # Expected output: 6
print(calculate_factorial(-1))  # Expected: Error message or specific value
