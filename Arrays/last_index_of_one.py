def lastIndex(s):
    count = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == '1':
            return i
    if '1' not in s:
        return -1


print(lastIndex('00010000'))
print(lastIndex('000'))
print(lastIndex('1'))

