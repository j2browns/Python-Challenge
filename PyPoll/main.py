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
    print(PyPoll_header)

#reading remainder of data set in csv into Monthly_data
#    Poll_data = list(csvreader)

    Candidate_List = []
    Candidate_Votes =[]
    for row in csvreader:
        Candidate = (row[2])
        if Candidate not in Candidate_List:
             Candidate_List.append(Candidate)
             Candidate_Votes.append(0)
        for i in range (0,len(Candidate_List)):
            if Candidate == Candidate_List[i]:
                Candidate_Votes[i] +=1

Total_Votes = 0
Percent_Votes = 0
Total_Votes = sum(Candidate_Votes)
Percent_Votes = [round(float(Candidate_Votes[i]/Total_Votes*100),3) for i in range(0,len(Candidate_Votes))]
#Percent_Votes = Candidate_Votes/Total_Votes*100 
Summary = { "Candidates:": Candidate_List,
            "Votes":Candidate_Votes
            }
print(Summary)
#print(Candidate_List)
#print(Candidate_Votes)
#print(Total_Votes)
#print(Percent_Votes)

