import os

import csv

election_data_csv = os.path.join("Resources","election_data.csv")


rowcount = 0
candidate = {}

with open (election_data_csv, newline='') as csv_file:

    csvreader = csv.reader(csv_file,delimiter=",")

    header = next(csvreader, None)

    counties = []
    candidate_list = []
    unique_candidate_names = []

    # The total number of votes cast
    for row in csvreader:
        rowcount += 1


    # A complete list of candidates who received votes
        candidate_list.append(row[2])
        if row[2] not in unique_candidate_names:
            unique_candidate_names.append(row[2])


    # The percentage of votes each candidate won
    for name in unique_candidate_names:
        candidate[name] = 0

    for item in candidate_list:
        candidate[item] += 1

    percentages = {}
    for name, vote_count in candidate.items():
        percentages[name] = (vote_count / rowcount) * 100


    # The total number of votes each candidate won
        # total numbers are in `candidate` dict


    # The winner of the election based on popular vote.
    person_with_most_votes = ""
    most_votes = 0
    for name, vote_count in candidate.items():
        if vote_count > most_votes:
            most_votes = vote_count
            person_with_most_votes = name


print(" Election Results")
print("--------------------")
print("Total Votes:", rowcount)
print("----------------------")
print("Percentages:", percentages)
print("Vote counts:", candidate)
print("----------------------------")
print("Winner:", person_with_most_votes)

