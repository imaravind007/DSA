def common_elements_in_sorted_array(arr1, arr2):
  p1 = 0
  p2 = 0
  res = []
  while p1 < len(arr1) and p2 < len(arr2):
    if arr1[p1] == arr2[p2]:
      res.append(arr1[p1])
      p1+=1
      p2+=1
    elif(arr1[p1]> arr2[p2]):
      p2+=1
    else:
      p1+=1
  return res

arr1 = [1,2,3,4,5,6,6,7]
arr2 = [2,4,5,7,7,8,9]
output = common_elements_in_sorted_array(arr1,arr2)
print(output)