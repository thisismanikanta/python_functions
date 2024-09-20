#write a function to find the largest and smallest numbers in a list

def large_small(list):
     largest=max(list)
     smallest=min(list)
     return largest,smallest
print("largest and smallest numbers are:",large_small([1,43,67,3,56,34,]))

#output:
largest and smallest numbers are:(67,1)
