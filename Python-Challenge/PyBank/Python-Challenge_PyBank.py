import os

import csv

budget_data_csv = os.path.join("Resources","budget_data.csv")
My_Report = open(os.path.join("Analysis", "Budget_Analysis.txt"), 'w')

total = 0 
months = 0
pre_rev = 0
total_ch = 0
inc = ["",0]
dec = ["",0]    

with open (budget_data_csv, newline='') as csv_file:

    csvreader = csv.reader(csv_file,delimiter=",")

    next(csvreader, None)   



    #The total number of months included in the dataset
    for row in csvreader:
        months += 1
        rev = int(row[1])
    

    #The net total amount of "Profit/Losses" over the entire period
        total += rev

    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
        change = rev - pre_rev

        if (pre_rev == 0):
            change = 0
        
        total_ch += change 
        pre_rev = rev

    #The greatest increase in profits (date and amount) over the entire period
        if(change>inc[1]):
            inc[1] = change
            inc[0] = row[0]


    #The greatest decrease in profits (date and amount) over the entire period
        if(change<dec[1]):
            dec[1] = change 
            dec[0] = row[0]

output = " Financial Analysis \n"
output += "--------------------\n"
output += f"Total Months: {months}\n"
output += f"Total: ${total}\n"
output += f"Average Change: ${(total_ch/(months-1)):,.2f}\n"
output += f"Greatest Increase in Profits: {inc[0]} (${inc[1]})\n"
output += f"Great Decrease in Profits: {dec[0]} (${dec[1]})\n"

print(output)
My_Report.write(output)
