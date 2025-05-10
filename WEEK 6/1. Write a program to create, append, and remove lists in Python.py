#creating an empty list
empty_List=[]
print("Empty List is:", empty_List)
#creating a list with elements
my_List=[10,507,"python"]
print("created list is:",my_List)
#Inserting new elements using append()
my_List.append(20)
my_List.append("program")
my_List.append([3,7])
print("After adding elements the new list is:",my_List)
#deleting elements using pop() method
d1=my_List.pop()
d2=my_List.pop(2)
#deleting the elements using remove
my_List.remove(10)
print("After deleting elements the new list is:",my_List)
#Removing all the elements using clear()
my_List.clear()
print("After removing all the elements the new list is:",my_List) 