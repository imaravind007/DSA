# Arun's Code
# question: https://practice.geeksforgeeks.org/problems/pythagorean-triplet3018/1
# Youtube link: https://www.youtube.com/watch?v=8tH4_7TL4fc - Just listen to the theory in this video, not the code

def p_triplets(arr):
  count=0
  d = "No"
  for i in range(len(arr)):
    arr[i] = pow(arr[i], 2)
  arr.sort()
  #print(arr)
  #return arr
  #print(len(arr))
  for i in range(len(arr)-1, 1, -1):
    a = 0
    b = i-1
    while(a<b):
      if (arr[a] + arr[b]) == arr[i]:
        count +=1
        #d = "Yes"
        a+=1
      elif (arr[a] + arr[b]) > arr[i]:
        b=b-1
      else: a=a+1
  return count

print(p_triplets([4, 5, 6, 3, 2]))