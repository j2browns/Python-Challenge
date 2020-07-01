# Homework 3 - Intro to Python: PyPoll
# Loading file
import os
import csv

# Path to collect data from the Resources folder
PyPoll_csv = os.path.join( "Resources", "election_data.csv")

#opening and reading file
with open(PyPoll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Reading Header
    PyPoll_header = next(csvfile) #reading header from file
    
    #checking Header is correct by printing.  To be removed or commented out in final version
    #print(PyPoll_header)

#reading remainder of data set in csv then getting candidates and totalling votes

    Candidate_List = []#will be list of candidates
    Candidate_Votes =[]#will be list of votes for candidate
    for row in csvreader:
        Candidate = (row[2])#getting candidate name
        if Candidate not in Candidate_List: #if candidate is not in list then add
             Candidate_List.append(Candidate) #add candidate
             Candidate_Votes.append(0) #add spot in votes
        for i in range (0,len(Candidate_List)):
            if Candidate == Candidate_List[i]: #finding index of candidate
                Candidate_Votes[i] +=1 #adding to counts for candidate

Total_Votes = 0
Percent_Votes = 0
Total_Votes = sum(Candidate_Votes)
Percent_Votes = [(Candidate_Votes[i]/Total_Votes*100) for i in range(0,len(Candidate_Votes))]
Percent_Votes = [round(Percent_Votes[i],2) for i in range(0,len(Candidate_Votes))]
# using dictionary comprehension 
# to convert lists to dictionary 
Summary = {Candidate_List[i]: [Candidate_Votes[i], Percent_Votes[i]] for i in range(len(Candidate_List))} 
Winner = max(Summary, key=Summary.get)
# Printing resultant dictionary 

#outputting to screen
print("\n")
print(f"Election Results\n")
print(f"*************************")
print(f"Total Votes: {Total_Votes}")
for key , value in Summary.items(): #printing out candidate, votes and percent votes
    print(f"Candidate: {key},  Votes: {value[0]},  Percent: {value[1]}%")

print(f"*************************")
print(f"Winner of election is: {Winner}\n")



