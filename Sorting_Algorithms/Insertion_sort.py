def insertion_sort(a):
    for i in range(len(a)):
        j = i-1;
        while j>=0 and a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            j=j-1;
    return a
a = [5, 4, 3, 2, 1]
output = insertion_sort(a)
print(output)
# Time complexity:O(n^2)
# Space complexity: 0(1)
