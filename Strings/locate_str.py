def strstr(s, x):
    n = len(x)
    for i in range(0, len(s)-n):
        if x == s[i:i+n]:
            return i
    return -1


print(strstr('GeeksForGeeks', 'For'))