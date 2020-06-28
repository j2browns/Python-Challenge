# Homework 3 - Intro to Python: PyBank
# Loading file
import os
import csv

# Path to collect data from the Resources folder
PyBank_csv = os.path.join( "Resources", "Budget_data.csv")

#opening and reading file
with open(PyBank_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Reading Header
    PyBank_header = next(csvfile) #reading header from file
    
    #checking Header is correct by printing.  To be removed or commented out in final version
    #print(PyBank_header)
    
    #reading remainder of data set in csv into Monthly_data
    Monthly_data = list(csvreader)

#Analysis below assumes data is given in months, sorted in order

print("Financial Analysis")
print("******************************")
#printing number of months
print(f"\nMonthly_data total list number: {len(Monthly_data)}")

Total_PL = 0 #tracking total profit loss
#Total_PL = sum(int(Monthly_data[1]))

for row in Monthly_data:
    Total_PL += int(row[1]) #addition is equivalent to c=c+a.  Assumes profit/loss is integer

print(f"\nTotal profit/Loss is: ${Total_PL}")

#*************************************************************************************
# Next section calculates difference in profit/loss between months.  Testing both List comprehension and for loop  
#using List comprehension to execute code
#Monthly_diff is the month to month difference if profit/loss calculated by list comprehension
Monthly_diff = [int(Monthly_data[i+1][1])-int(Monthly_data[i][1]) for i in range(0,len(Monthly_data)-1)]

#Calculating average monthly change
Total_change = 0 #to sum total change for calculating average
for row in Monthly_diff:
    Total_change += float(row)

Average_change = float(Total_change/(len(Monthly_diff)))
Average_change = round(Average_change,2)
print(f"\nAverage Change in Profit: ${Average_change}")

#Average_change = mean(Monthly_diff)
Max_diff = max(Monthly_diff)
Min_diff = min(Monthly_diff)

Monthly_diff.insert(0,0) #inserting extra row at beginning so Monthly_data and difference are same index
#this insert is done after other calcs so does not affect calc of max or min

Test1 = False
Test2 = False

for i in range(0,len(Monthly_data)):
    if Monthly_diff[i] == Max_diff:
        Month_max = [Monthly_data[i][0],Monthly_diff[i]]
        Test1 = True
    if Monthly_diff[i]==Min_diff:
        Month_min = [Monthly_data[i][0],Monthly_diff[i]]
        Test2=True
    if Test1 and Test2: #if found both max and min months then stop
        break

print(f"Greatest increase in profit  {Month_max[0]} with ${Month_max[1]}")
print(f"Greatest decrease in profit  {Month_min[0]} with ${Month_min[1]}")
print("")


#using for loop to accomplish same thing as list comprehension statement.  To make sure understand
#Monthly_change=[]
#for i in range(0,len(Monthly_data)-1):
#    Monthly_change.append(int(Monthly_data[i+1][1])-int(Monthly_data[i][1]))
#Monthly_change.insert(0,0)
#print(f"Monthly change in for loop {len(Monthly_change)}")

