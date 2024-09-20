#write a function to find the gcd of two numbers


def func(a,b):
    if a==0:
      return b
    elif b==0:
      return a
    else:
      return func(b,a%b)
print(func(10,5))

#output:
5
