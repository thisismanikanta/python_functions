#write a function to find the second largest number in a list

def second_large(list1):
   large=max(list1)
   list1.remove(large)
   second_large=max(list1)
   return second_large
l=second_large([1,5,2,43,3,45])
print(l)


#output:
43
