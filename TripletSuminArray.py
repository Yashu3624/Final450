class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
          
        # Your Code Here
          a = sorted(A)
          for i in range(n-2):
               j = i+1
               k = n-1
               while(j<k):
                    if a[i]+a[j]+a[k] == 'X':
                         return 1
                    elif a[i]+a[j]+a[k] <= 'X':
                         j += 1
                    else:
                         k -= 1
          return 0    
        
