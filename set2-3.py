"""With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this
list after removing all duplicate values with original order reserved.
"""
a =[12,24,35,24,88,120,155,88,120,155]
new_list=[]
for i in a:
    if i not in new_list:
        new_list.append(i)
print(new_list)
print(new_list[::-1])