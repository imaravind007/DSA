def reverse_A_string(S):
  a = S.split(".")
  b = []
  for i in range(len(a)-1, -1, -1):
    print(i)
    b.append(a[i])
    print(b)
  return ".".join(b)

S = 'i.like.this.program.very.much'
print(reverse_A_string(S))