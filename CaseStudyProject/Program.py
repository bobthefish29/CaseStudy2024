#David
#lotoya
#Kerry


#This is where the main program is going to live,

#i just hope we dont have to bring it into anaconda to make it run or anything



##################--------------------Imports--------------------------##########################
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


##################--------------------Vars--------------------------##########################

abbreviation_to_name = {
    "AK": "Alaska",
    "AL": "Alabama",
    "AR": "Arkansas",
    "AZ": "Arizona",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "IA": "Iowa",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "MD": "Maryland",
    "ME": "Maine",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MO": "Missouri",
    "MS": "Mississippi",
    "MT": "Montana",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NV": "Nevada",
    "NY": "New York",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VA": "Virginia",
    "VT": "Vermont",
    "WA": "Washington",
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "WY": "Wyoming",
    "DC": "District of Columbia",
    "AS": "American Samoa",
    "GU": "Guam GU",
    "MP": "Northern Mariana Islands",
    "PR": "Puerto Rico PR",
    "VI": "U.S. Virgin Islands"
}

#print(len(abbreviation_to_name))


#############---------This is just the csv data frams----------------------#########
high_Grad_rate = pd.read_csv('Data/high income.csv')
low_Grad_rate = pd.read_csv('Data/low income.csv')

#################---------This is adding the whole city csv
all_City_csv = pd.read_csv('Data/uscities.csv')
all_city_arrary = all_City_csv.to_numpy()
# print(all_city_arrary[12][0])


firstLoop = 0
nextLoop = 0

wasIf = 0

for c in all_City_csv["city"]:
    for i in high_Grad_rate["Name"]:
        if(i == c):
            print(firstLoop,' ', nextLoop, "it was in at ", c, wasIf)
            wasIf += 1

        nextLoop += 1

    
    firstLoop += 1


# for i in range(0,len(abbreviation_to_name)):
#     for c in range(0, len(all_city_arrary)):
#         print(i,c)

# print(np.isin(all_city_arrary[1][1], all_city_arrary[0][0]))

# if(np.isin(all_city_arrary[0][0], all_city_arrary[0][0])):
#     print('me')
# else:
#     print('not me')

#print(all_city_arrary[0])

#running 30k times or each city is being persented


# for i in range(0, len(high_Grad_rate)):
#     for c in all_City_csv["city"]:
#         print(i,' ',c)


# for i in range(0, len(all_city_arrary)):

#     for c in all_City_csv["city"]:
#         print(c)
#         # if(all_city_arrary[i][0] == c):
#         #     print("is in", c ," with ", i)
#         #     print(all_city_arrary[i])
#     # if(np.isin(i, all_City_csv["city"])):
        



# for i in range(0, len(all_city_arrary)):

#     for n in high_Grad_rate["Name"]:
#         print(n)

#     print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHERE", i)

    

#     # if(np.isin(all_City_csv["city"].any(), i)):
#     #     print(i)
#     # else:
#     #     print("umm")



# if(np.isin(high_Grad_rate["Name"].any(), all_city_arrary[0] )):
#     print('True')


#     # if(all_city_arrary[indexer][0] == ):
#     #     print(i)




#     indexer += 1

#     # if(i == "RI"):
#     #     print(all_City_csv["city"])




#################-------------------This is the sorted by the names----------------------###################
sorted_high_Name = high_Grad_rate.sort_values(by=['Name'], ascending=True)
sorted_Low_Name = low_Grad_rate.sort_values(by=['Name'], ascending=True)

##############----------This is the total rec------------#########
high_total_rec = len(high_Grad_rate["College_Graduation_Rate_rP_gP_p75"])-1
low_total_rec = len(low_Grad_rate["College_Graduation_Rate_rP_gP_p25"]) - 1












##############----------This is the avg of the american-----------#########
avg_of_america_high = high_Grad_rate["College_Graduation_Rate_rP_gP_p75"].sum() / high_total_rec
avg_of_america_low = low_Grad_rate["College_Graduation_Rate_rP_gP_p25"].sum() / low_total_rec

plt.scatter(avg_of_america_high, avg_of_america_high)
plt.scatter(avg_of_america_low, avg_of_america_low)

plt.title('Graduation Rate: Low income and high income familys')

plt.xlabel('Graduration rate')
plt.ylabel('Graduration rate')


plt.show()


##################--------------------Functions--------------------------##########################

#this is a data frame of all the states and there aberavation





##################--------------------Main Code--------------------------##########################

#print(low_Grad_rate.head())



#this is just to have them sorted



#print("high")
#print(high_Grad_rate["Name"][39])

#print("High")
#print(sorted_high["Name"][39])

#total = 0

#for i in high_Grad_rate["Name"]:
    #total += 1
    
#print(total)

# for i in high_Grad_rate:
#     for n in i:
#         print(i)
    # for n in :

    #     print(high_Grad_rate[i])
    #     # if high_Grad_rate > high_Grad_rate["Name"]:

    #     #     print("swaped")
    #     #     # Swap elements if they are in the wrong order
    #     #     high_Grad_rate[i], high_Grad_rate[i + 1] = high_Grad_rate[i + 1], high_Grad_rate[i]



# def bubble_sort_df(df, column_name):
#     print('In df')
#     for i in range(len(df) - 1):
#         print('first loop', (i-1))

#         # for j in range(len(df) - i - 1):
#         # print('secoend loop')
#         if df.loc[i, column_name] > df.loc[i + 1, column_name]:
#             print('if')
#             df.loc[i], df.loc[i + 1] = df.loc[i + 1].copy(), df.loc[i].copy()

#     return df



# df_sorted = bubble_sort_df(high_Grad_rate, 'Name')
# print(high_Grad_rate)
# print(df_sorted)

# print('made it')


"""
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

"""

#sorted_high.groupby(sorted_high["College_Graduation_Rate_rP_gP_p75"])

# sorted_high.sum()


#print(sorted_high["College_Graduation_Rate_rP_gP_p75"].sum() / total)
#print(sorted_Low["College_Graduation_Rate_rP_gP_p25"].sum() / total)


#plt.scatter((sorted_high["College_Graduation_Rate_rP_gP_p75"].sum() / total), (sorted_high["College_Graduation_Rate_rP_gP_p75"].sum() / total), c="Green")
#plt.scatter((sorted_Low["College_Graduation_Rate_rP_gP_p25"].sum() / total), (sorted_Low["College_Graduation_Rate_rP_gP_p25"].sum() / total), c="Red")

#plt.bar((sorted_high["College_Graduation_Rate_rP_gP_p75"].sum() / total), (sorted_Low["College_Graduation_Rate_rP_gP_p25"].sum() / total))
#plt.bar((sorted_Low["College_Graduation_Rate_rP_gP_p25"].sum() / total), (sorted_high["College_Graduation_Rate_rP_gP_p75"].sum() / total))

# sorted_high["College_Graduation_Rate_rP_gP_p75"].hist(1, bins=1000)
# sorted_high[1].hist(dist2, bins=n_bins)

#plt.hist(sorted_high["College_Graduation_Rate_rP_gP_p75"], sorted_Low["College_Graduation_Rate_rP_gP_p25"])
#plt.scatter(sorted_high["College_Graduation_Rate_rP_gP_p75"], sorted_Low["College_Graduation_Rate_rP_gP_p25"], c="Blue")

#plt.scatter(sorted_Low["College_Graduation_Rate_rP_gP_p25"], sorted_high["College_Graduation_Rate_rP_gP_p75"], c="Red")
# plt.scatter(sorted_Low["College_Graduation_Rate_rP_gP_p25"], sorted_Low["College_Graduation_Rate_rP_gP_p25"], c="Green")


# for i, label in enumerate(sorted_high["Name"]):
#     if(sorted_high["Name"][i] == "New York"):
#         print(sorted_high["Name"][i])
#         plt.annotate(label, (sorted_high["College_Graduation_Rate_rP_gP_p75"][i], sorted_high["College_Graduation_Rate_rP_gP_p75"][i]))




#this is how we will lable all the items
# plt.xlabel('Graduation rate')
# plt.ylabel('Graduation rate')

# plt.show()