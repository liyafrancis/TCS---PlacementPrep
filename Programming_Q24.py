# Write a program that takes an array that denotes the daily closing prices of a stock to determine the maximum profit by buying and selling one share of the stock.

# Sample Input 0
# 310,315,275,260,270,290,230,255,250
# Sample Output 0
# 30

ls=list(map(int,input().split(",")))
min_val=float('inf')
profit=0
for i in ls:
    min_val=min(min_val,i)
    profit=max(profit,i-min_val)

print(profit)


