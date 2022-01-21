# Given an array of size N-1 such that it only contains distinct integers
# in the range of 1 to N. 
# Find the missing element.
def missing_number(a):
  n = len(a)
  print(a)
  sum_of_n_numbers = (n*(n+1))/2
  for i in range(len(a)-1):
    sum_of_n_numbers -= a[i]
  
  return sum_of_n_numbers

def missing_number_2(a):
  n = len(a)
  sum_of_n_numbers = sum(a)
  total =  (n+2)*(n+1)/2
  return total - sum_of_n_numbers



a = [2,1,3,4]
print(a)
output_1 = missing_number(a)
output_2 = missing_number_2(a)
print(output_1)
print(output_2)