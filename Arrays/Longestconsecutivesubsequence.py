 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        #code here
        res = []
        arr = list(set(arr))
        arr = sorted(arr)
        for i in range(1,len(arr)):
          if arr[i]-arr[i-1]==1:
            c += 1
          else:
            res.append(m+1)
            c = 0
        res.append(m+1)
        return max(res)
            
            
        
