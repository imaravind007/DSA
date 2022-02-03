raw = ["Apple\n", "One\n" , " \n", "Apple\n", "TWO\n"]

s = []
for i in range(len(raw)):
    s.append(raw[i].replace('\n', ''))

s1 = []
for i in range(len(s)):
    s[i] = s[i].lower()
    if (s[i] == ' '):
        s1 += " "
    elif(i==0):
        s1 = s[i]
    else:
        if(s[i-1] != " "):
            s[i]=s[i][0].upper() + s[i][1:]
        s1 += s[i]
print(s1)
