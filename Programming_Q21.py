# Given two strings s and t, print "true" if t is an anagram of s, and "false" otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Sample Input 0
# anagram
# nagaram
# Sample Output 0
# true

# Sample Input 1
# rat
# car
# Sample Output 1

# false
s1=input()
s2=input()
if(sorted(s1)==sorted(s2)):
    print("true")
else:
    print("false")
