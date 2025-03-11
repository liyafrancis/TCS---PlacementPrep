# Write a program to display all the multiples of 3 within the range n and m. Read the value of n and m from the first two lines of the console as input. 
# Print all the multiples of 3 within the range of n and m as output (exclude n and m).

# Sample Input 0
# 10
# 50
# Sample Output 0
# 12 15 18 21 24 27 30 33 36 39 42 45 48 

x=int(input())
y=int(input())

first=x%3
if first!=3:
    first=x-first
x=first+3

for i in range(x,y,3):
    print(i,end=" ")
    
    
