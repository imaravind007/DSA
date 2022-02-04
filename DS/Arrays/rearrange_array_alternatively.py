# Given a sorted array of positive integers.
#  Your task is to rearrange  the array elements alternatively 
# i.e first element should be max value, second should be min value, 
# third should be second max, fourth should be second min and so on.
def rearrange_Alternatively(a):
  b = []
  a.sort()
  left = 0 
  right = len(a)-1
  while left < right:
    b.append(a[right])
    b.append(a[left])
    right-=1
    left+=1
    if left == right:
      b.append(a[left])
  return b 


a= [10,20,30,40,50,60,70,80,90,100,110]
output = rearrange_Alternatively(a)
print(output)

