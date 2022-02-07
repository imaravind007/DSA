def first_maximum_repeating_element(arr):

  dic = {}
  for idx, value in enumerate(arr):
    if value not in dic:
      dic[value]=1
    else:
      dic[value] += 1
  print(dic)
  # return dic[1]

  # Maximum frequency:
  max_count = 0
  for idx, value in enumerate(arr):
    if (max_count < dic[value]):
      max_count = dic[value]
  

  return max_count

arr = [4,4,4,4,1,1,1,1,0,0,0,0,0,0,0]
output = first_maximum_repeating_element(arr)
print(output)