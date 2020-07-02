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
print(f"*************************")
for key , value in Summary.items(): #printing out candidate, votes and percent votes
    
    #formatting statement below creates nice aligned table.  : is space, < is left aligned 10 is 10 spaces, s is string
    #d is for integer, f is for flot.  > is right align.  2 with f is for 2 digits.  
    print('Candidate: {:<10s} Votes: {:<10d} Percent: {:>10.2f}%'.format( key, value[0], value[1],2))
     
print(f"*************************")
print(f"Winner of election is: {Winner}\n")


#outputting results.  The \n character does a break line to move to next line in file
PyPoll_Out = os.path.join( "analysis", "PyPoll_Summary.txt")
text_file = open(PyPoll_Out, 'w') 
text_file.write("\n")
text_file.write(f"Election Results\n")
text_file.write(f"*************************\n")
text_file.write(f"Total Votes: {Total_Votes}\n")
text_file.write(f"*************************\n")
for key , value in Summary.items(): #printing out candidate, votes and percent votes
    #text_file.write(f"Candidate: {key},  Votes: {value[0]},  Percent: {value[1]}%\n")
    text_file.write('Candidate: {:<10s} Votes: {:<10d} Percent: {:>10.2f}%\n'.format( key, value[0], value[1],2))
text_file.write(f"*************************\n")
text_file.write(f"Winner of election is: {Winner}\n")

text_file.close()
