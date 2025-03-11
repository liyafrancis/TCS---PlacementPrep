# Write a program to find the average of n numbers using a while loop. Read an integer, n from the console, which will be the number of values.
# Write a while loop to read n numbers from the console and find the average of all these numbers. Print the average value as the output with a precision of 3 decimal places.

# Sample Input 0
# 3
# 4.5
# 5.5
# 6
# Sample Output 0
# The average is: 5.333

n=int(input())
tot=0;i=0
while i<n:
    num=float(input())
    tot=tot+num
    i=i+1
total=tot/n
print(f"The average is: {total:.3f}")
