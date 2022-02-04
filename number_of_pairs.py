# # Brute force
# def no_of_pairs(x, y):
#     count = 0
#     for i in x:
#         for j in y:
#             if i**j > j**i:
#                 count += 1
#     return count

## Optimized solution
## O(n log n + m log n)
from bisect import bisect

def no_of_pairs(x, y):
    count = 0
    x.sort()
    y.sort()
    # the rule is not valid for 1, 2, 3, 4 (check from table)
    # so we create an array to store the counts of 0, 1, 2, 3, 4 in y
    # instead of looping it again in the next for loop, to reduce time complexity
    exception_array = [0] * 5
    for idx in range(len(y)):
        if y[idx] < 5:
            exception_array[y[idx]] += 1

    for i in range(len(x)):
        if x[i] == 0:
            continue
        if x[i] == 1:
            count += exception_array[0]
            continue

        j = bisect(y, x[i])
        count += len(y) - j
        count += exception_array[1]
        if x[i] == 2:
            count -= exception_array[3] + exception_array[4]
        if x[i] == 3:
            count -= exception_array[2]
    return count


print(no_of_pairs([10, 19, 18], [11, 15, 9]))