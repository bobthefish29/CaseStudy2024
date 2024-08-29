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
high_Grad_rate = pd.read_csv('Data/high income.csv')
low_Grad_rate = pd.read_csv('Data/low income.csv')


##################--------------------Functions--------------------------##########################



##################--------------------Main Code--------------------------##########################

#print(low_Grad_rate.head())

#this is just to have them sorted
sorted_high = high_Grad_rate["Name"].sort_values()
sorted_Low = low_Grad_rate["Name"].sort_values()


#print(sorted_Low)







############-----------this whole section is for a scatter plot------------#############
#the blue and green section is just reversed of eachother, the red is having the 
plt.scatter(low_Grad_rate["College_Graduation_Rate_rP_gP_p25"], high_Grad_rate["College_Graduation_Rate_rP_gP_p75"], c="Blue")
plt.scatter(high_Grad_rate["College_Graduation_Rate_rP_gP_p75"], low_Grad_rate["College_Graduation_Rate_rP_gP_p25"], c="Green")

#this section is based on just the numbers and the numbers. this might be more acuret for a line graph than a scatter plot
plt.scatter(high_Grad_rate["College_Graduation_Rate_rP_gP_p75"], high_Grad_rate["College_Graduation_Rate_rP_gP_p75"], c="Orange")
plt.scatter(low_Grad_rate["College_Graduation_Rate_rP_gP_p25"], low_Grad_rate["College_Graduation_Rate_rP_gP_p25"], c="red")

#this is adding lables to all the plot points for the csv 1 file based on name
#its looping through all the data in the names catogory
for i, label in enumerate(high_Grad_rate["Name"]):
    #this is adding all the lables for all the items in the csv
    #plt.annotate(label, (high_Grad_rate["College_Graduation_Rate_rP_gP_p75"][i], high_Grad_rate["College_Graduation_Rate_rP_gP_p75"][i]))

    #here is for if the value is new york it would lable there
    if(high_Grad_rate["Name"][i] == "New York"):
        plt.annotate(label, (high_Grad_rate["College_Graduation_Rate_rP_gP_p75"][i], high_Grad_rate["College_Graduation_Rate_rP_gP_p75"][i]))



#this is getting the lable for new your on the low income table
for i, label in enumerate(low_Grad_rate["Name"]):
    if(low_Grad_rate["Name"][i] == "New York"):
        plt.annotate(label, (low_Grad_rate["College_Graduation_Rate_rP_gP_p25"][i], low_Grad_rate["College_Graduation_Rate_rP_gP_p25"][i]))



#this is how we will lable all the items
plt.xlabel('Graduation rate: L,H,H,L')
plt.ylabel('Graduation rate: H,L,H,L')

plt.show()