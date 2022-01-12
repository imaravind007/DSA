# Bubble sorting:
# Think about the range and i and j variable in this loop. 
def bubble_sort(a):
	for i in range(len(a)):
		for j in range(len(a)-i-1):
			if(a[j]>a[j+1]):
#In one step we can swap the element in python:
				a[j], a[j+1] = a[j+1], a[j]
	return a
array = [1, 2, 3, 4, 5, 6, 1]
output = bubble_sort(array)
print(output)
# Output:
# [1, 1, 2, 3, 4, 5, 6]
# Time complexity O(n^2)
# Space complexity O(1): We are not using any extra space.
