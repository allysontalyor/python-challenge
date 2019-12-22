#dependencies
import os
import csv

#create path to where the csv file is located locally
csvpath=os.path.join('..','/Users/allysontalyor/Documents/Bootcamp_Assignments/python-challenge/PyPoll','election_data.csv')

#open the file using a csv reader
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)
    #this line recognizes the first row as a header and automatically advances to the next row
    header=next(csvreader)
    #print(f"CSV Header: {header}")

    #count is the total vote count
    count=0
    #this dictionary, keys are the candidate names and the values are lists containing the voter ID numbers
    candidates={}
    for row in csvreader:
        
        #these create the 'candidates' dictionary defined above
        if row[2] not in candidates:
            candidates.update({row[2]:[row[0]]})
        else:
            candidates[row[2]].append(row[0])

        
        #a way to calculate the total votes
        count+=1

#this function will calculate the total number of votes for each candidate and the percentage of the
#total votes obtained by a candidate
def CandidateStats(cand_list):
    total=int(len(cand_list))
    percentage=round((len(cand_list)/count*100),3)
    print(cand+':     '+str(percentage)+'%   ('+str(total)+')')
   
#printing the report of the election
print('Election Results')
print('_________________________')
print('')
print('Total Votes:   '+str(count))
print('_________________________')
print('')

#value to hold the number of votes obtained by the winner
max_votes=0
#this variable should hold the winners name
winner="winner"

#This loop will go through each key:value pain in the dictionary and apply the CandidateStats function
for cand in candidates:
    CandidateStats(candidates[cand])

    #this conditional will determine which candidate was the winner!
    if int(len(candidates[cand]))>max_votes:
        max_votes=int(len(candidates[cand]))
        winner=cand

print('_________________________')
print('')
print('Winner:   '+winner)
print('_________________________')

