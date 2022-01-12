# Merge Sort:
# It is a recursive algorithm, first, we have to divide the array then we have to merge two sorted arrays. 
def mergesort(arr):
    if len(arr) > 1:
        last = len(arr)
        first = 0 
        mid = (first + last)//2
        L = arr[:mid]
        R = arr[mid:]
        mergesort(L)
        mergesort(R)
        i, j, k = 0, 0, 0
        while (i< len(L) and j < len(R)):
            if L[i] > R [j]:
                arr[k] = R[j]
                j+=1
                k+=1
            else:
                arr[k] = L[i]
                i+=1
                k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j <len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    return arr

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
output = mergesort(arr)
print(output)
