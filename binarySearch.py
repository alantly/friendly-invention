

def evenOddBinarySearchMain(arr, low, high):
  if len(arr) == 1:
    print "Not enough values"
  if arr[0]%2 == 0 and arr[-1]%2 == 1:
    return evenOddBinarySearch(arr, low, high)
  else:
    print "Switch does not exist"

def evenOddBinarySearch(arr, low, high):
  if (low > high):
    return low
  middle = (low+high)/2
  if arr[middle]%2 == 0:
    return evenOddBinarySearch(arr,middle+1,high)
  else:
    return evenOddBinarySearch(arr,low,middle-1)

a = [2,8,2,4,5]
b = evenOddBinarySearchMain(a,0,len(a)-1)
print(b)




def binarySearchBound(arr, key, low, high):
  if (low > high):
    return low
  middle = (low+high)/2
  if arr[middle] > key:
    return binarySearchBound(arr,key,low,middle-1)
  else:
    return binarySearchBound(arr,key,middle+1,high)

a = [0,0,0,1,1,1,1,3,3]
b = binarySearchBound(a,0,0,len(a)-1)
print(b)
