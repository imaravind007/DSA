def first_recurring_character(s):
  dic= {}
  for i in s:
    if i in dic:
      return i
    else:
      dic[i] = 1
s = 'ABCDEA'
output = print(first_recurring_character(s))