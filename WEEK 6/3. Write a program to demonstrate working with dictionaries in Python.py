#empty dictionary
my_dict={}
print("Empty dictionary is:",my_dict)
#dictionary with integer keys
my_dict={1:'apple',2:'ball'}
print("dictionary with integer keys",my_dict)
#dictionary with mixed keys
my_dict={'name':'rishi',1:[2,4,3]}
print("dictionary with mixed keys",my_dict)
#using dicy.fromkeys()
my_dict=dict.fromkeys("abcd",'alphabet')
print("dictionary created by using dict.fromkeys method=",my_dict)
#using get method
my_dict={'name':'jack','age':25}
print(my_dict['name']) #ouput jack
#changing and adding dictionary elements
my_dict['age']=18 #upadte vaue
my_dict['class']="B.Tech" #updating vlaue
print("After changing and adding the values,the new dictionary=",my_dict)
#using items()
print("items in the dictionary is:",my_dict.items())
#using keys()
print("Keys in the dictionary is:",my_dict.keys())
#using values()
print("values in the dictionary is:",my_dict.values())