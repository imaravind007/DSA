# def distinct(str):
#     output = 1
#     sub_str = []
#
#     for i in range(len(str)-1):
#         sub = str[i]
#         for j in range(i+1, len(str)):
#             if str[j] not in sub:
#                 sub = sub + str[j]
#             else:
#                 break
#         sub_str.append(sub)
#     output = max(sub_str, key=len)
#
#     return len(output)

def distinct(str):
    # Creating a set to store the last positions of occurrence
    seen = {}
    maximum_length = 0

    # starting the initial point of window to index 0
    start = 0

    for end in range(len(str)):

        # Checking if we have already seen the element or not
        if str[end] in seen:
            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, seen[str[end]] + 1)

        # Updating the last seen value of the character
        seen[str[end]] = end
        maximum_length = max(maximum_length, end - start + 1)
    return maximum_length


#print(distinct('qwertyuioplkjh'))
print(distinct('aaadfcxxx'))