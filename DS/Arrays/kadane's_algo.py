#Maximum Contigious Subarray:
#This is solved using the Dynammic Prograaming 
# Understanding the previous sub problem to solve the cuurent sub-problem. 
#Time Complexity: O(n)
#Space Complexity: O(1)
def kadans_algorithm(a):
  local_minimum =  a[0]
  global_maximum = a[0]
  for i in range(1, len(a)-1):
    local_minimum = max(a[i], local_minimum+a[i])
    if local_minimum > global_maximum:
      global_maximum=local_minimum
  return global_maximum

a = [-2, 3, 2, -1, 6, 7, 8]
# a = [-2, -3, 4, -1, -2, 1, 5, -3]
output = kadans_algorithm(a)
print(output)