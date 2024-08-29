#David
#lotoya
#Kerry




#This is where the main program is going to live,

#  i just hope we dont have to bring it into anaconda to make it run or anything




##################--------------------Imports--------------------------##########################
import matplotlib.pyplot as plt

import numpy as np

import pandas as pd


##################--------------------Vars--------------------------##########################
csv1 = pd.read_csv('Data/high income.csv')
csv2 = pd.read_csv('Data/low income.csv')


##################--------------------Functions--------------------------##########################

# csv1_ind = csv1.sort_values(["College_Graduation_Rate_rP_gP_p75","Name"])

# Print the top few rows
#print(csv1["College_Graduation_Rate_rP_gP_p75"])


##################--------------------Main Code--------------------------##########################






##this whole section is for a scatter plot
plt.scatter(csv2["College_Graduation_Rate_rP_gP_p25"], csv1["College_Graduation_Rate_rP_gP_p75"])
plt.scatter(csv1["College_Graduation_Rate_rP_gP_p75"], csv2["College_Graduation_Rate_rP_gP_p25"])

plt.scatter(csv1["College_Graduation_Rate_rP_gP_p75"], csv1["College_Graduation_Rate_rP_gP_p75"])
plt.scatter(csv2["College_Graduation_Rate_rP_gP_p25"], csv2["College_Graduation_Rate_rP_gP_p25"])

#this is adding lables to all the plot points for the csv 1 file based on name
for i, label in enumerate(csv1["Name"]):
    #plt.annotate(label, (csv1["College_Graduation_Rate_rP_gP_p75"][i], csv1["College_Graduation_Rate_rP_gP_p75"][i]))

    #here is for if the value is new york it would lable there
    if(csv1["Name"][i] == "New York"):
        plt.annotate(label, (csv1["College_Graduation_Rate_rP_gP_p75"][i], csv1["College_Graduation_Rate_rP_gP_p75"][i]))
        plt.annotate(label, (csv2["College_Graduation_Rate_rP_gP_p25"][i], csv2["College_Graduation_Rate_rP_gP_p25"][i]))


#this is how we will lable all the items
plt.xlabel('X lable')
plt.ylabel('ylabel')

plt.show()