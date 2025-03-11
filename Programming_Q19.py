# In this challenge, determine the minimum number of chairs needed to accommodate all cricket players in a new team relaxation room. The room does not have any chairs at the beginning.
# There will be a string of simulations. A combination of four characters describes each simulation:
# C, R, U, and L
# • C - A new player arrives in the room. If there is a chair available, the player takes it. Otherwise, a new one is purchased.
# • R - A player goes to play cricket, freeing up a chair.
# • U - A player arrives at the room after playing. If there is a chair available, the player takes it. Otherwise, a new one is purchased.
# • L - A player leaves the room for practice, freeing up a chair.

# Sample Input 1
# CCRURC
# Sample Output 1
# 2

seq=input()
available=0
total=0

for i in seq:
    if i in ['C','U']:
        if available>0:
            available=available-1
        else:
            total=total+1
    elif i in ['R','L']:
        available=available+1
print(total)
