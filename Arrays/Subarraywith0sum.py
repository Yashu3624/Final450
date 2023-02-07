class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        dic = {}
        sum = 0 
        for i in range(len(arr)):
          sum += arr[i]
          if sum == 0 or sum in dic:
            return True
            dic[sum] = 1
            
        return False
            
