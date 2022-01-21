# Virtually divide the array into two half(Sorted, Unsorted)
# In Unsorted array: Place the minimum element at the start of the array(sort it in ascending order)
def selection_sort(a):
	for i in range(len(a)):
		fixed = i
		for j in range(i+1, len(a)):
			if(a[fixed]>a[j]):
				a[fixed], a[j] = a[j], a[fixed]
	return a
array = [1, 2, 3, 4, 5, 6, 1]
output = selection_sort(array)
print(output)
# Output:
# [1, 1, 2, 3, 4, 5, 6]
# Time Complexity:O(n^2)
# Space complexity:O(1)
