#write a program to define a function with multiple return values

def function(a,b,c):
  if a>b and a>c:
      return a
  elif b>a and b>c:
      return b
  else:
      return c
print(function(1,2,3))

#output:
3
