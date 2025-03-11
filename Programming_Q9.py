# Write a program to find the product of a set of real numbers.
# Read the number of values n from the console in the first line. For the next "n" lines, read the real numbers one by one. Print the product of the n numbers on the console as output.
# The output value should be rounded off to two decimal places.

# Sample Input 0
# 4
# 3.2
# 6.6
# 4.3
# 5.1
# Sample Output 0
# The product of the numbers is: 463.16

n=int(input())
product=1
for i in range(n):
    num=float(input())
    product=product*num
print(f"The product of the numbers is: {product:.2f}")
    
