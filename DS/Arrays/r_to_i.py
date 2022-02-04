# Convert roman to integers:
# First store all the elements in the dictionary. Check the first and the next letter in the upcoming string. 
# If the first value is greater than the nxt value then add the value to the result variable. 
# Or deduct the element from the result.



def convert_roman_to_integer(st):
    dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    res = 0
    for i in range(len(st)):
        value = dict[st[i]]
        if  i+1 < len(st) and dict[st[i+1]] > value:
            res-=value
        else:
            res+=value
            
    return res


st = 'VILMC'
output = convert_roman_to_integer(st)
print(output)
