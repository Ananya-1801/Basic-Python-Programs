# Write a program in Python to accept a list and create another
# list to store the indices of the non-zero values in the list.

list1=eval(input("Enter a list:"))
list2=[]
for i in list1:
    if(i!=0):
        a=list1.index(i)
        list2.append(a)
        continue
print(list2)
        
