# Arun's Code
# Question: https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1
# For further clarity on this problem: YouTube Link for this  problem: https://www.youtube.com/watch?v=KOglcclYgXI&t=752s


def rearrange(arr):
  min, max = 0, len(arr)-1
  k = arr[max] + 100
  for i in range(len(arr)):
    if i%2==0:
      arr[i] = arr[i]+((arr[max]%k)*k)
      max-=1
    else:
      arr[i] = arr[i] + ((arr[min]%k)*k)
      min+=1
  arr[:] = [(x // k) for x in arr]
  return arr

print(rearrange([2, 3, 4, 5, 7, 9, 10, 12]))