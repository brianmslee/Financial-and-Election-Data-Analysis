import os 

import csv 

election_data_csv = os.path.join("Resources","election_data.csv")

rowcount = 0
candidate = [""]

with open (election_data_csv, newline='') as csv_file:

    csvreader = csv.reader(csv_file,delimiter=",")

    header = next(csvreader, None)   

    # The total number of votes cast
    for row in csvreader:
        rowcount += 1
    

    # A complete list of candidates who received votes
    if row[2] != row[2] 

    #The percentage of votes each candidate won


    #The total number of votes each candidate won


    #The winner of the election based on popular vote.


print(" Election Results ")
print("--------------------")
print("Total Votes:" , rowcount)
print("---------------------")

