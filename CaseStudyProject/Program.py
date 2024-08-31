#David
#lotoya
#Kerry



##################--------------------Imports--------------------------##########################
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


##################------------this is adding the csv files--------###############3

#############---------This is just the csv data frams----------------------#########
high_Grad_rate = pd.read_csv('Data/high income.csv')
low_Grad_rate = pd.read_csv('Data/low income.csv')

#################---------This is adding the whole city csv-----------------------
all_City_csv = pd.read_csv('Data/uscities.csv')
all_city_arrary = all_City_csv.to_numpy()

##############--------this bit of code is for the functions that are going to be running-----------############3


#this is just making the city and name data into a series so we could check if its in the other data
high_series1 = pd.Series(all_City_csv["city"])
high_series2 = pd.Series(high_Grad_rate["Name"])

#just to have low (Just in case) 
low_series1 = pd.Series(all_City_csv["city"])
low_series2 = pd.Series(low_Grad_rate["Name"])

#Find common elements in both high and low lists
common_high_elements = np.intersect1d(high_series1, high_series2)
common_low_elements = np.intersect1d(low_series1, low_series2)

#Convert the result to a DataFrame for both high and low
matching_df_high = pd.DataFrame(common_high_elements, columns=['city'])
matching_df_low = pd.DataFrame(common_low_elements, columns=['city'])


##############--------------Important functions--------------#############

#the functions are really just the same thing but for high and low

#This is making a list of the towns that are in both, of the dataFrams for (high,low) and wholeCityCSV
def find_Town_high_list(StateADB):
    appenedList = []
    for i in range(0, len(all_City_csv)):
        if(all_city_arrary[i][2] == StateADB):
            #this if statment------------VVVVVVVVVVV
            if(all_city_arrary[i][1] in matching_df_high.values):
                appenedList.append(all_city_arrary[i][1])
    return appenedList
def find_Town_low_list(StateADB):
    appenedList = []
    for i in range(0, len(all_City_csv)):
        if(all_city_arrary[i][2] == StateADB):
            #this if statment------------VVVVVVVVVVV
            if(all_city_arrary[i][1] in matching_df_low.values):
                appenedList.append(all_city_arrary[i][1])
    return appenedList

#this is just for returning the aberage of the the highlist towns  find_avg_high_gradRate(This is the town list you want)
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
    #returning the total devided by the len of the lists to get the avg
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
    #returning the total devided by the len of the lists to get the avg
    return total / len(lowList)

#This is to find the state avg, based on the abreavation EX.('RI') you put in
def find_avgHigh_based_On_adv(highadb):
    total = 0
    stateAdb = find_Town_high_list(highadb)
    for i in range(0, len(stateAdb)):
        for l in range(0, len(high_Grad_rate["Name"])):
            if(stateAdb[i] == high_Grad_rate["Name"][l]):
                try:
                    rate = float(high_Grad_rate["College_Graduation_Rate_rP_gP_p75"][l])
                    # Check if the rate is NaN
                    if not math.isnan(rate):
                        total += rate
                except ValueError:
                    # Handle the case where conversion to float fails
                    print(f"Invalid value for conversion: {high_Grad_rate['College_Graduation_Rate_rP_gP_p75'][l]}")
    return total / len(stateAdb)
def find_avgLow_based_On_adv(lowadb):
    total = 0
    stateAdb = find_Town_low_list(lowadb)
    for i in range(0, len(stateAdb)):
        for l in range(0, len(low_Grad_rate["Name"])):
            if(stateAdb[i] == low_Grad_rate["Name"][l]):
                try:
                    rate = float(low_Grad_rate["College_Graduation_Rate_rP_gP_p25"][l])
                    # Check if the rate is NaN
                    if not math.isnan(rate):
                        total += rate
                except ValueError:
                    # Handle the case where conversion to float fails
                    print(f"Invalid value for conversion: {low_Grad_rate['College_Graduation_Rate_rP_gP_p25'][l]}")
    return total / len(stateAdb)


##############----------This is the avg low vs the avg high in america all of america-----------#########

###########------------------------the first graph is to show what it would look like on a scatter plot---------##########
avg_of_america_high = high_Grad_rate["College_Graduation_Rate_rP_gP_p75"].sum() / (len(high_Grad_rate["College_Graduation_Rate_rP_gP_p75"]) - 1)
avg_of_america_low = low_Grad_rate["College_Graduation_Rate_rP_gP_p25"].sum() / (len(low_Grad_rate["College_Graduation_Rate_rP_gP_p25"]) - 1)
#green is high, red is low income
plt.scatter(avg_of_america_high, avg_of_america_high, c='green', label='High')
plt.scatter(avg_of_america_low, avg_of_america_low, c='red', label='Low')
plt.title('Graduation Rate for: Low income and high income familys')
plt.xlabel('Graduration rate')
plt.ylabel('Graduration rate')
plt.text(avg_of_america_high, avg_of_america_high, "{0:.2f}".format(avg_of_america_high), fontsize=10, ha='right')
plt.text(avg_of_america_low, avg_of_america_low, "{0:.2f}".format(avg_of_america_low), fontsize=10, ha='right')
plt.legend()
plt.show()


#########################--------this graph is to show what it would look like in a bar graph--------############3
#adding the data for the bargraph
categories = ['High Income', 'Low Income']
averages = [avg_of_america_high, avg_of_america_low]
#green is high, red is low income
colors = ['green', 'red']
plt.bar(categories, averages, color=colors)
plt.title('Graduation Rate for Low and High Income Families')
plt.xlabel('Income Category')
plt.ylabel('Graduation Rate')
# Add text annotations on the bars
for i, value in enumerate(averages):
    plt.text(i, value, "{0:.2f}".format(value), ha='center', va='bottom')
plt.show()




################------------this section is for the different states of america--------------###########
#########--------this is if we want it to be a scatter plot-----------------#########
#its hard to fallow

#there is no data for HI so we cant use it lol
states = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
    'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
]
for state in states:
    # print(state)
    avg_high = find_avgHigh_based_On_adv(state)
    avg_low = find_avgLow_based_On_adv(state)
    # Scatter plot
    plt.scatter(avg_high, avg_low, label=state)
    # Add text labels
    plt.text(avg_high, avg_low, state, fontsize=9, ha='right')

plt.ylabel('Low Income : Graduation Rate')
plt.xlabel('High Income : Graduation Rate')

# Show the plot
plt.show()


#################----------This is if we want the data to be in a bar graph-----------##################
#this is a lot easer to fallo

#this is calulationg the avarage for each state and making it into a list for both high and low
high_income_avgs = [find_avgHigh_based_On_adv(state) for state in states]
low_income_avgs = [find_avgLow_based_On_adv(state) for state in states]

#This is just making the data for the bar graph to show what we want
x = np.arange(len(states))
width = 0.4  # Width of bars

#This is making the bar graph
fig, graph = plt.subplots(figsize=(14, 8))
highIncome = graph.bar(x - width/2, high_income_avgs, width, label='High Income', color='Green')
lowIncome = graph.bar(x + width/2, low_income_avgs, width, label='Low Income', color='red')

# Add titles and labels
graph.set_xlabel('State')
graph.set_ylabel('Graduation Rate')
graph.set_title('Graduation Rates by State for High and Low Income Families')

# Add x-tick labels
graph.set_xticks(x)
graph.set_xticklabels(states, rotation=90)

# Add legend
graph.legend()

# Add text labels
for bars in [highIncome, lowIncome]:
    for bar in bars:
        height = bar.get_height()
        graph.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height:.2f}', ha='center', va='bottom')

# Show the plot
plt.tight_layout()#just making it close together
plt.show()






#################################--------------End of project----------################################################






#this section of code is the dark space, its stuff that i was playing around with and just left the comment incase i want to come back to it


















# plt.scatter(find_avgHigh_based_On_adv('AL'), find_avgLow_based_On_adv('AL'), label="AL")
# plt.scatter(find_avgHigh_based_On_adv('AK'), find_avgLow_based_On_adv('AK'))
# plt.scatter(find_avgHigh_based_On_adv('AZ'), find_avgLow_based_On_adv('AZ'))
# plt.scatter(find_avgHigh_based_On_adv('AR'), find_avgLow_based_On_adv('AR'))


# plt.scatter(find_avgHigh_based_On_adv('CA'), find_avgLow_based_On_adv('CA'))
# plt.scatter(find_avgHigh_based_On_adv('CO'), find_avgLow_based_On_adv('CO'))
# plt.scatter(find_avgHigh_based_On_adv('CT'), find_avgLow_based_On_adv('CT'))

# plt.scatter(find_avgHigh_based_On_adv('DE'), find_avgLow_based_On_adv('DE'))
# plt.scatter(find_avgHigh_based_On_adv('DC'), find_avgLow_based_On_adv('DC'))

# plt.scatter(find_avgHigh_based_On_adv('FL'), find_avgLow_based_On_adv('FL'))



# Georgia: GA 
# Hawaii: HI 
# Idaho: ID 
# Illinois: IL 
# Indiana: IN 
# Iowa: IA 
# Kansas: KS 
# Kentucky: KY 
# Louisiana: LA 
# Maine: ME 
# Maryland: MD 
# Massachusetts: MA 
# Michigan: MI 
# Minnesota: MN 
# Mississippi: MS 
# Missouri: MO 
# Montana: MT 
# Nebraska: NE 
# Nevada: NV 
# New Hampshire: NH 
# New Jersey: NJ 
# New Mexico: NM 
# New York: NY 



# plt.scatter(find_avgHigh_based_On_adv('RI'), find_avgLow_based_On_adv('RI'), c='green')
# plt.scatter(find_avgHigh_based_On_adv('CA'), find_avgLow_based_On_adv('CA'), c='green')
# plt.scatter(find_avgHigh_based_On_adv('MA'), find_avgLow_based_On_adv('MA'), c='green')
# plt.scatter(find_avgHigh_based_On_adv('CT'), find_avgLow_based_On_adv('CT'), c='green')



# plt.scatter(find_avgLow_based_On_adv('NY'), find_avgLow_based_On_adv('NY'), c='Red')
# plt.scatter(find_avgLow_based_On_adv('RI'), find_avgLow_based_On_adv('RI'), c='Red')
# plt.scatter(find_avgLow_based_On_adv('CA'), find_avgLow_based_On_adv('CA'), c='Red')
# plt.scatter(find_avgLow_based_On_adv('MA'), find_avgLow_based_On_adv('MA'), c='Red')
# plt.scatter(find_avgLow_based_On_adv('CT'), find_avgLow_based_On_adv('CT'), c='Red')


# plt.xlabel('High Income Graduation Rate')
# plt.ylabel('Low Income Graduation Rate')
# plt.show()

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