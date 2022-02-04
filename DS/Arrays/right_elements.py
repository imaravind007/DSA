# Count elements in the right are higher 
def count_higher_element(a):
    n = len(a)
    counter = [0]*n
    # for i in range(n):
    #     counter[i] = 0 
    for i in range(n):
        for j in range(i+1, n):
            if (a[j]>a[i]):
                counter[i]+=1
    return counter
a = [2, 4, 5, 6, 7,20, 8, 9, 10, 12]
output = count_higher_element(a)
print(output)
# [9, 8, 7, 6, 5, 0, 3, 2, 1, 0]
