#Leaders in an array
# Given an array of distinct integers.
# The task is to count all the triplets such
# that sum of two elements equals the third element.
def leaders_in_an_array(a):
  res = []
  a.reverse()
  max_value = -99
  for k,value in enumerate(a):
    if value > max_value:
      max_value = value
      res.append(max_value)
  return res[::-1]
 

a = [16,17,4,3,5,2]
b = [1,2,3,4,0]
output1 = leaders_in_an_array(b)
print(output1)