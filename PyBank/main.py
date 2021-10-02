
#import modules
import csv
import os

# source to read csv data
fileLoad = os.path.join("Resources", "budget_data.csv")

# variables
totalMonths = 0
netTotal = 0
monthlyChange = []
months = []

# output file for budget analysis
outputFile = os.path.join("Analysis", "budget_analysis.txt")

# read the csv file
with open(fileLoad) as budgetData:
    #create a csv reader object
    csvreader = csv.reader(budgetData)

    #read the header row
    header = next(csvreader)

    # move to first row
    firstRow = next(csvreader)

    # add 1 to the count of total months
    totalMonths += 1 

    # calculate the net Total from budget data
    netTotal += float(firstRow[1])

    # establish previous total revenue- found in index 1
    previousTotal = float(firstRow[1])
    

    for row in csvreader:
        # add 1 to the count of total months
        totalMonths += 1 

        # calculate the net Total from budget data
        netTotal += float(row[1])

        # calulate the net change
        netChange = float(row[1])- previousTotal
        # add change to list of monthly changes
        monthlyChange.append(netChange)

        #add the first month that a change occurs
        months.append(row[0])

        #update previous Total
        previousTotal = float(row[1])

# Calculate the average net change per month
avgChangePerMonth = sum(monthlyChange) / len(monthlyChange)

# month and value of greatest increase/decrease
greatestIncrease = [months[0], monthlyChange[0]]
greatestDecrease = [months[0], monthlyChange[0]]

# loop to caclulate the index of greatest and least monthly changes
for m in range(len(monthlyChange)):
    if(monthlyChange[m]) > greatestIncrease[1]:
        greatestIncrease[1] = monthlyChange[m]
        greatestIncrease[0] = months[m]

    if(monthlyChange[m] < greatestDecrease[1]):
        greatestDecrease[1] = monthlyChange[m]
        greatestDecrease[0] = months[m]

# generate output
output = (
    f"Financial Analysis \n"
    f"-----------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${netTotal:.0f} \n"
    f"Average Change: ${avgChangePerMonth:.2f}\n"
    f"Greatest Increase = {greatestIncrease[0]} Amount (${greatestIncrease[1]:.0f})\n"
    f"Greatest Decrease = {greatestDecrease[0]} Amount (${greatestDecrease[1]:.0f})"
    )

#print output to terminal
print(output)

# export output to the budget analysis text file
with open(outputFile, "w") as textFile:
    textFile.write(output)