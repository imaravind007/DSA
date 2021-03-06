#reverse an array with the given block size
#Time Complexity 0(n)
#Space Complexity 0(1)

def swap(left, right, arr):
  while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left+=1
    right-=1
  return arr

def reverse_an_array(arr, a):
  for i in range(0, len(arr)-a+1, a):
    arr = swap(i, i+a-1, arr)
  return arr
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 3 
output = reverse_an_array(arr, a)
print(output)