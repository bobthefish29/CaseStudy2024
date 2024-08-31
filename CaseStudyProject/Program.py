#David
#lotoya
#Kerry



##################--------------------Imports--------------------------##########################
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


##################--------------------Vars--------------------------##########################


#print(len(abbreviation_to_name))


#############---------This is just the csv data frams----------------------#########
high_Grad_rate = pd.read_csv('Data/high income.csv')
low_Grad_rate = pd.read_csv('Data/low income.csv')

#################---------This is adding the whole city csv-----------------------
all_City_csv = pd.read_csv('Data/uscities.csv')
all_city_arrary = all_City_csv.to_numpy()

high_series1 = pd.Series(all_City_csv["city"])
high_series2 = pd.Series(high_Grad_rate["Name"])

low_series1 = pd.Series(all_City_csv["city"])
low_series2 = pd.Series(low_Grad_rate["Name"])

#Find common elements
common_high_elements = np.intersect1d(high_series1, high_series2)
common_low_elements = np.intersect1d(low_series1, low_series2)

#Convert the result to a DataFrame
matching_df_high = pd.DataFrame(common_high_elements, columns=['city'])
matching_df_low = pd.DataFrame(common_low_elements, columns=['city'])


#the two functions here are really the same code, it just incase the matching dataFrames have a different value it would show itn in the low or high
def find_Town_high(townadbv):
    appenedList = []
    for i in range(0, len(all_City_csv)):
        if(all_city_arrary[i][2] == townadbv):
            #this if statment------------VVVVVVVVVVV
            if(all_city_arrary[i][1] in matching_df_high.values):
                appenedList.append(all_city_arrary[i][1])
    return appenedList
def find_Town_low(townadbv):
    appenedList = []
    for i in range(0, len(all_City_csv)):
        if(all_city_arrary[i][2] == townadbv):
            #this if statment------------VVVVVVVVVVV
            if(all_city_arrary[i][1] in matching_df_low.values):
                appenedList.append(all_city_arrary[i][1])
    return appenedList

#this is just for returning the aberage of the the highlist towns
def find_avg_high_gradRate(highList):
    total =0
    for i in range(0, len(highList)):
        for l in range(0, len(high_Grad_rate["Name"])):
            if(highList[i] == high_Grad_rate["Name"][l]):
                try:
                    rate = float(high_Grad_rate["College_Graduation_Rate_rP_gP_p75"][l])
                    # Check if the rate is NaN
                    if not math.isnan(rate):
                        total += rate
                except ValueError:
                    # Handle the case where conversion to float fails
                    print(f"Invalid value for conversion: {high_Grad_rate['College_Graduation_Rate_rP_gP_p75'][l]}")
    return total / len(highList)
def find_avg_low_gradRate(lowList):
    total =0
    for i in range(0, len(lowList)):
        for l in range(0, len(low_Grad_rate["Name"])):
            if(lowList[i] == low_Grad_rate["Name"][l]):
                try:
                    rate = float(low_Grad_rate["College_Graduation_Rate_rP_gP_p25"][l])
                    # Check if the rate is NaN
                    if not math.isnan(rate):
                        total += rate
                except ValueError:
                    # Handle the case where conversion to float fails
                    print(f"Invalid value for conversion: {low_Grad_rate['College_Graduation_Rate_rP_gP_p25'][l]}")
    return total / len(lowList)

###############################################################################################################################################

riListHigh = find_Town_high('RI')
riListlow = find_Town_high('RI')


print(find_avg_high_gradRate(riListHigh))
print(find_avg_low_gradRate(riListlow))


# bigList = []

# bigList.append(find_Town_high('LA'))
# bigList.append(find_Town_high('RI'))

# print(bigList)


# # Rename columns in high_Grad_rate to match the columns in all_City_csv for merging
# df1_renamed = high_Grad_rate.rename(columns={'Name': 'city'})

# # Merge matching_df with df1_renamed
# merged_df = matching_df.merge(df1_renamed, on='city', how='left', indicator=True)

# # Filter rows that are only in the original DataFrame and not in the other
# non_matching_df = merged_df[merged_df['_merge'] == 'left_only']

# # Convert the non-matching DataFrame to a list of dictionaries
# non_matching_list = non_matching_df.drop(columns=['_merge']).to_dict(orient='records')

# print("\nNon-matching records:")
# print(non_matching_list)






# high_series1 = pd.Series(all_City_csv["city"])
# high_series2 = pd.Series(high_Grad_rate["Name"])

# # Find common elements
# common_high_elements = np.intersect1d(high_series1, high_series2)
# print("Common elements:", common_high_elements)

# # Convert the result to a DataFrame
# matching_df = pd.DataFrame(common_high_elements, columns=['city'])
# print("Matching DataFrame:")
# print(matching_df)

# # Rename columns in high_Grad_rate to match the columns in all_City_csv for merging
# df1_renamed = high_Grad_rate.rename(columns={'Name': 'city'})
# print("Renamed DataFrame for merging:")
# print(df1_renamed)

# # Merge matching_df with df1_renamed
# merged_df = matching_df.merge(df1_renamed, on='city', how='left', indicator=True)
# print("Merged DataFrame:")
# print(len(merged_df))

# # Filter rows that are only in the original DataFrame and not in the other
# non_matching_df = merged_df[merged_df['_merge'] == 'left_only']
# print("Non-matching DataFrame:")
# print(non_matching_df)

# # Convert the non-matching DataFrame to a list of dictionaries
# non_matching_list = non_matching_df.drop(columns=['_merge']).to_dict(orient='records')
# print("\nNon-matching records:")
# print(non_matching_list)


# df1_renamed = high_Grad_rate.rename(columns={'Name': 'city'})

# df1_renamed = df1_renamed.drop_duplicates()

# matching_df = df1_renamed.merge(all_City_csv, on='city', how='inner')

# df1_renamed = matching_df.drop_duplicates()

# Print the resulting DataFrame with matching cities and their state abbreviations
# print("Matching DataFrame:")
# print(matching_df)







# for i in common_high_elements_list:
#     print(i)



# print(all_City_csv["state_id"])


# riList = []
# for i in range(0, len(all_city_arrary)):

#     if(all_city_arrary[i][2] == 'NY'):
#         riList.append(all_city_arrary[i][1])

# # print(riList)
# # print(all_City_csv["state_id"])


# riTotal = 0

# for i in range(0, len(high_Grad_rate)):
#     #print(high_Grad_rate['Name'][i])

#     for r in riList:
#         # print(high_Grad_rate["College_Graduation_Rate_rP_gP_p75"][i])
#         # print(r)
#         if(high_Grad_rate['Name'][i] == r):
#             print(r)
#             # riTotal += high_Grad_rate["College_Graduation_Rate_rP_gP_p75"][i]


# print(riTotal * 2)



#     #for sn in range(0, len(addbrevLIst)):
        
#         #if(all_city_arrary[i][2] == addbrevLIst[sn]):
            

#         #all_city_arrary[i][2]
#     print(c)
#     # nextLoop = 0
#     # for i in high_Grad_rate["Name"]:
        
#     #     if(i == c):
#     #         print(firstLoop,'',nextLoop, "it was in at ", c, wasIf)
#     #         wasIf += 1

#     #     nextLoop += 1

    
#     # firstLoop += 1
# print(riList)

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