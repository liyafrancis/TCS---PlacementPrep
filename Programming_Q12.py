# Write a program to check whether the given integer is a prime number or not. Read an integer from the console as input.
# If the integer is a prime number, print "n is a prime number", where n is the value of the integer. Else, print "n is not a prime number".

# Sample Input 0
# 7
# Sample Output 0
# 7 is a prime number

n=int(input())
flag=0
for i in range(2,n//2+1):
    if n%i==0:
        flag=1
        
if flag==1:
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")
