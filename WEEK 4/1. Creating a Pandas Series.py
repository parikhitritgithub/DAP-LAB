import pandas as pd  # Importing the Pandas library
import numpy as np   # Importing NumPy

# Creating an empty Series
ser = pd.Series()
print("Pandas Series: ", ser)

#2nd one
# Creating a Series from a NumPy array
data = np.array(['g', 'e', 'e', 'k', 's'])
ser = pd.Series(data)
print("Pandas Series:\n", ser)

# List of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']

# Creating a DataFrame from the list
df = pd.DataFrame(lst)
print(df)

#3rd one
# Initializing data
data = {'Name': ['Tom', 'nick', 'krish', 'jack'], 'Age': [20, 21, 19, 20]}

# Creating DataFrame
df = pd.DataFrame(data)
print(df)

#4th one
# Dictionary of lists
dict_data = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
             'degree': ["MBA", "BCA", "M.Tech", "MBA"],
             'score': [90, 40, 80, 98]}

df = pd.DataFrame(dict_data)
print(df)
