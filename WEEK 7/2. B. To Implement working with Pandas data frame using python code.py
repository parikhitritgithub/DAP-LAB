import pandas as pd

# Creating the data dictionary
data = {
    "Name": ["Ram", "Subash", "Raghul", "Arun", "Deepak"],
    "Age": [24, 25, 24, 26, 25],
    "CGPA": [9.5, 9.3, 9.0, 8.5, 8.8]
}

# Creating the DataFrame
t = pd.DataFrame(data)

# Changing the index to start from 1 instead of 0
t.index += 1

# Printing the DataFrame
print(t)
