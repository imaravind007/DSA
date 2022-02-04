# Arun's code
# Question: https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
# Youtube Link: https://www.youtube.com/watch?v=NWMcj5QFW74&t=127s

def merge2(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    s1, s2, e1, e2 = 0, 0, n - 1, m - 1
    while (s1 < n and s2 < m):
        if (arr1[s1] > arr2[s2]):
            arr1[e1], arr2[s2] = arr2[s2], arr1[e1]
            s2 += 1
            e1 -= 1
        else:
            s1 += 1
    arr1.sort()
    arr2.sort()
    print(arr1)
    return arr2


print(merge2([2, 5, 7, 7, 10], [3, 6, 9, 12]))