#creating an empty tuple
empty_tup=()
print("Empty tuple=",empty_tup)
#creating single element tuple
single_tup=(10,)
print("single element tuple=",single_tup)
#creating a tuple with multiple elements
my_Tup=(10,3.7,'program','a')
print("Tuple with multiple elements is:",my_Tup)
print("Length of the tuple is:",len(my_Tup))
T1=(10,20,30,40,70.5,33.3)
print("Maximum value of the tuple T1 is:",max(T1))
print("Minimum value of the tuple T1 is:",min(T1))
str1='tuple'
T=tuple(str1)#convering string into tuple
print("After converting a string into tuple,the new tuple is:",T)
L=[2,4,6,7,8]
T2=tuple(L)#convering string into tuple
print("After converting a List into tuple,the new tuple is:",T2)