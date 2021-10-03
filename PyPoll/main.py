# import modules
import csv
import os

# source to read the csv data
fileLoad = os.path.join("Resources", "election_data.csv")

# variables
totalVotes = 0
candidates = []
candidateVotes = {}
winningTotal = 0
winningCandidate = []

# output file for election analysis
outputFile = os.path.join("Analysis", "election_analysis.txt")

# read csv file
with open(fileLoad) as electionData:
    csvreader = csv.reader(electionData)

    # read in the header row
    header = next(csvreader)

    # rows are lists
        # index 0 is voter Id
        # index 1 is County
        # index 2 is user vote (candidate)
    #for each row
    for row in csvreader:
        # add on to the total vote
        totalVotes +=1

        # see if Candidate is already in List of Candidates & add if not
        if row[2] not in candidates:
            candidates.append(row[2])

            # add value to dictonary
            candidateVotes[row[2]] = 1
        
        else: 
            # if the candidate is already in list add vote to candidate vote count
            candidateVotes[row[2]] += 1

candidate_output = ""

for candidate in candidateVotes:
    # vote count and percentage of votes
    votes = candidateVotes.get(candidate)
    votePercent = float(votes)/ float(totalVotes) * 100.00
    candidate_output += f"{candidate}: {votePercent:.3f}% ({votes})\n"
   
   # compare candidate vote totals to find Winner
    if votes > winningTotal:
       #update the new winning total
       winningTotal = votes
       #update the winning Candidate
       winningCandidate = candidate

winningCandidateOutput = f"Winner: {winningCandidate}\n"
# generate output
output = (
    f"Election Results \n"
    f"-------------------------\n"
    f"Total Votes: {totalVotes}\n"
    f"--------------------------\n"
    f"{candidate_output}"
    f"--------------------------\n"
    f"{winningCandidateOutput}"
    f"--------------------------\n"
)

# print output to terminal/ console
print(output)

# export output to election analysis file
with open(outputFile, "w") as textfile:
    textfile.write(output)

