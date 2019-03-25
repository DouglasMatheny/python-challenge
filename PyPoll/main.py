import os
import csv

#Declare and initialize variables
election_data_csv_path = os.path.join("Resources", "election_data.csv")
results_path = os.path.join("Resources", "results.txt")

#Declare and initialize variables
counts = {}
vote_counts = int(0)
winning_votes = int(0)
winner = ""

#Read in the file and load counts dictionary.
with open(election_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        counts[str(row[2])] = counts.get(str(row[2]),0)+1

#Tally up the results and determine the winner
for key in counts:
    vote_counts = vote_counts+counts[key]
    if counts[key] > winning_votes:
        winning_votes = counts[key]
        winner = key


#Print and save the results
with open(results_path,"w") as f:
     f.write(f"Election Results\n")
     print(f"Election Results")
     f.write(f"-------------------------\n")
     print(f"-------------------------")
     f.write(f"Total Votes: {vote_counts}\n")
     print(f"Total Votes: {vote_counts}")
     f.write(f"-------------------------\n")
     print(f"-------------------------")
     for key in counts:
         f.write(f"{key}: {round((counts[key]/vote_counts)*100,4)}% ({counts[key]})\n")
         print(f"{key}: {round((counts[key]/vote_counts)*100,4)}% ({counts[key]})")
     f.write(f"-------------------------\n")
     print(f"-------------------------")
     f.write(f"Winner: {winner}\n")
     print(f"Winner: {winner}")
     f.write(f"-------------------------\n")
     print(f"-------------------------")
