# our task is to create a Python script that analyzes the records to calculate each of the following:

    # The total number of months included in the dataset

    # The net total amount of "Profit/Losses" over the entire period

    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

    # The greatest increase in profits (date and amount) over the entire period

    # The greatest decrease in profits (date and amount) over the entire period


#import modules
import csv
import os

# source to read csv data
fileLoad = os.path.join('Resources', 'budget_data.csv')

# variables
totalMonths = 0
netTotal = 0

# output file for budget analysis
outputFile = os.path.join('Analysis', "budget_analysis.txt")
# read the csv file

with open(fileLoad) as budgetData:
    #create a csv reader object
    csvreader = csv.reader(budgetData)

    #read the header row
    header = next(csvreader)

    for row in csvreader:
        # add 1 to the count of total months
        totalMonths += 1 

        # calculate the net Total from budget data
        netTotal += float(row[1])

# generate output
output = (
    f"Financial Analysis \n"
    f"-----------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: {netTotal:.0f}"
    )
#print output to terminal
print(output)

# export output to the budget analysis text file
with open(outputFile, "w") as textFile:
    textFile.write(output)