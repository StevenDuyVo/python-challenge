import csv

#Import path
csv_file_path = r"C:\Users\python-challenge-main\PyPoll\Resources\election_data.csv"

#Variables
total_votes = 0
max_votes = 0
candidate_votes = {}
candidates = []
winner = ""

#Read dataset
with open(csv_file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  

    #Calculate total votes
    for row in csvreader:
        total_votes = total_votes +  1
        candidate = row[2]
        #If candidate is not in list, add them
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] = candidate_votes[candidate] + 1

#Calculate percentage votes
percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

#Determine winner
for candidate, votes in candidate_votes.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

#Print to terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentage_votes[candidate]}% ({candidate_votes[candidate]})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#Print to text file
output_path = r"python-challenge-main\PyPoll\analysis"
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("----------------------------")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write("----------------------------")
    for candidate in candidates:
        txtfile.write(f"{candidate}: {percentage_votes[candidate]}% ({candidate_votes[candidate]})")
    txtfile.write("----------------------------")
    txtfile.write(f"Winner: {winner}")
    txtfile.write("----------------------------")