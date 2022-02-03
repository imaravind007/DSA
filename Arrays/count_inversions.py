## Brute force
# from bisect import bisect
# def inversion(arr):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             if arr[i] > arr[j]:
#                 count += 1
#     return count

# print(inversion([2, 3, 4, 5, 6]))

## Merge sort solution
# O(n log n)
# Indirectly tracking inversions through merge sort
def merge(A, aux, low, mid, high):
    k = i = low
    j = mid + 1
    inversionCount = 0

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            i = i + 1
        else:
            aux[k] = A[j]
            j = j + 1
            inversionCount += (mid - i + 1)
        k = k + 1

    while i <= mid:
        aux[k] = A[i]
        k = k + 1
        i = i + 1


    for i in range(low, high + 1):
        A[i] = aux[i]
    return inversionCount

def mergesort(A, aux, low, high):

    if high <= low:  # if run size <= 1
        return 0

    mid = low + ((high - low) >> 1)
    inversionCount = 0

    inversionCount += mergesort(A, aux, low, mid)  # split/merge left half
    inversionCount += mergesort(A, aux, mid + 1, high)  # split/merge right half
    inversionCount += merge(A, aux, low, mid, high)  # merge the two half runs

    return inversionCount


A = [8, 4, 2, 1]
aux = A.copy()
print(mergesort([8, 4, 2, 1], aux, 0, len(A) - 1))