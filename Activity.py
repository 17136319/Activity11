import numpy as np
import matplotlib.pyplot as mp
import pandas as pd

# x = np.array([1,2,3])
# y = np.array(['nick','jane','eric'])
# mp.plot(y,x)
# mp.show()
#  Question 1
# Import the data from your CSV file into a Pandas Dataframe
tips = pd.read_csv('./class activity 11 data/tips.csv')
Data = pd.DataFrame(tips)
# Question 2
# Add a new calculated column to the dataframe
tips["Total_Payed"] = (tips["tip"] /  (tips["total_bill"]+tips["tip"])) * 100

#  Question 3
#  Create a subset of the data based on a condition
sex = tips["sex"] == "Male"
gender = tips[sex]

# Question 4
# Calculate the correlation coefficient between 
# two columns and show whether a significant correlation
# exists (correlation coefficient values less than +0.8
# or greater than -0.8 are not considered significant).
x = gender["total_bill"]
y = gender["Total_Payed"]
hello = np.corrcoef(x,y)
print(hello)




# Question 5
# mp.scatter(x,y)
# mp.title("CorrTest")
# mp.xlabel('Totalbills (thousands)')
# mp.ylabel("Total Payed") 
# mp.show()



# --------------------------------------------------------------------
gk = Data.groupby(["day","sex"]).sum()
print(gk)
# riend = tips.corr(method='pearson')
# tips = tips[tips["sex"] == "male"]
# friend = pd.DataFrame(data=titanic)  .equals('Male')
# titanic["types"] = friend
# titanic["test"]=titanic["age"] * 10
# Headsex
# # test = Head = 'male'
# print(titanic)
# print(gender.head(3))
# print(tips.head(5))

