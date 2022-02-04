# x + y = target 
# y = target - x 
def two_sum(a,target):
  dic = {}
  for idx, value in enumerate(a):
    if (target-a[idx]) in dic:
      return dic[target-a[idx]], idx
    else:
      dic[a[idx]] = idx
      print(dic)

a = [1, 2, 3, 4, 5]
print(two_sum(a, 5))