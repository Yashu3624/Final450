#User function Template for python3

def isSubset( a1, a2, n, m):
  a1 = sorted(a1)
  a2 = sorted(a2)
  for i in a2:
    if not in a1:
      return 'No'
    if i in a1:
      a1.remove(i)
  return 'Yes' 
