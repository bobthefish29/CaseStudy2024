import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np


raceTotals_withEducation = pd.read_csv('Data/raceGradrate.csv')
raceTotals = pd.read_csv('Data/raceAlone.csv')

races = [i for i in raceTotals]
races_Total =[raceTotals[l][0] for l in raceTotals]


#just a bubble sorting algurthum, it checks if the next index is bigger then the currerent index than switches them if it is
#it takes in two lists, that have to be the same lenght. than it sorts the items based on the values
def bubble_sort_races(arr_num, arr2_name):
    for i in range(0, len(arr_num) - 1):
        for l in range(0, len(arr_num) - i - 1):
            if arr_num[l] > arr_num[l + 1]:
                arr2_name[l], arr2_name[l + 1] = arr2_name[l + 1], arr2_name[l]
                arr_num[l], arr_num[l + 1] = arr_num[l + 1], arr_num[l]


###############-------This is the graph for the total amout of people that graduated based on race
#this is just replacing the "," with blank spaces so we can sort the values
int_averages = [int(a.replace(',', '')) for a in races_Total]
bubble_sort_races(int_averages, races)

#incase we want to view the data with , in it
# sorted_averages = [f'{num:,}' for num in int_averages]
#this is the graph tho
plt.bar(races, int_averages)
for i, value in enumerate(int_averages):
    plt.text(i, value, "{0}".format(value), ha='center', va='bottom')
plt.title("Graduation based on race in 2022")
plt.ylabel("In hundred millions")
plt.show()

##########3---------------This graph is for based on bachulers degree-------#############

White_Bachelor = raceTotals_withEducation['White_Bachelor']
Black_Bachelor = raceTotals_withEducation['Black_Bachelor']
American_Native_Bachelor = raceTotals_withEducation['American_Native_Bachelor']
Asian_Bachelor = raceTotals_withEducation['Asian_Bachelor']
Hawaiian_Bachelor = raceTotals_withEducation['Hawaiian_Bachelor']
other_Bachelor = raceTotals_withEducation['other_Bachelor']
Hispanic_Bachelor = raceTotals_withEducation['Hispanic_Bachelor']

bachelorListRace = ["White","Black","Native","Asian","Hawaiian","Other","Hispanic"]
bachelorList = [White_Bachelor[0],Black_Bachelor[0],American_Native_Bachelor[0],Asian_Bachelor[0],Hawaiian_Bachelor[0],other_Bachelor[0],Hispanic_Bachelor[0]]


int_bachelorList = [int(a.replace(',', '')) for a in bachelorList]
bubble_sort_races(int_bachelorList, bachelorListRace)

plt.bar(bachelorListRace, int_bachelorList)
for i, value in enumerate(int_bachelorList):
    plt.text(i, value, "{0}".format(value), ha='center', va='bottom')
plt.title("Graduation with bachelor in 2022")
plt.ylabel("In millions")
plt.show()

