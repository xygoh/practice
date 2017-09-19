# takes in an array of characters and returns the first occurence of a not repeating character
# returns '_' if none found

# list comprehension solution
def firstNotRepeatingCharacter(s):
    arr = [c for c in s if s.count(c)==1]
    if len(arr)>0:
        return arr[0]
    return '_'


# faster solution using ordered dictionary (collections)
import collections
def firstNotRepeatingChar_Fast(s):
  od=collections.orderedDict()
  for i in s:
    if i not in od:
      od[i]=1
    else:
      od[i]+=1
  
  for k,v in od.items():
    if v==1:
      return k
  
  return '_'
