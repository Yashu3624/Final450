from collections import Counter

class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        c = n//k
        o  = 0
        l = Counter(arr)
        v = list(l.values())
        for i in range(len(v)):
          if v[i]>c:
            s += 1
        return s
