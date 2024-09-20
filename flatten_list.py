#write a function to flatten list of lists into single list

def flat_list(*args):
   list2=[]
   for i in args:
     list2+=i
   return list2
l=flat_list([1,2,3],[4,5,6],[7,8,9])
print(l)

#output:
[1,2,3,4,5,6,7,8,9]
