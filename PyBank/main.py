#depencies (lets us create file pathways across operating systems..I think)
import os
import csv

#Get where the file is currently working at
#print(os.getcwd())
#displaying all the things inside current directory
#print(os.listdir())

#create path to indicate where the csv file is located locally
#I left this as is, but I do understand how to shorten this!
csvpath=os.path.join('..','/Users/allysontalyor/Documents/Bootcamp_Assignments/python-challenge/PyBank','budget_data.csv')

#open file and read using CSV reader function
with open('budget_data.csv',newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)
    #this line recognizes the header and advances to the next line containing data
    header=next(csvreader)
    #print(f"CSV Header: {header}")

    #create a list to contain all of the elements in the first column (row[0])
    months=[]
    #starting value for the sum
    total=0
    #variable used to identify the greatest increase in the change amount
    #amount set to zero initially
    greatest_increase=0
    #this variable is used to hold the value for the month/year associated
    #with the greatest increase.  I put in Jan 2010, but it can be any string value
    greatest_increase_month="Jan 2010"
    #this variable is used to hold the value for the month/year associated
    #with the greatest decrease.  Can be any string value
    greatest_decrease=0
    greatest_decrease_month="Jan 2010"
    #when calculating the change value, I set the prev_value=0, so that
    #there is a numeric value to subtract from the first value.  The first
    #value is later removed, so this numberic value does not matter
    prev_value=0
    #list to hold the calculated change value
    change_values=[]


#for loop to run through each row in a csv file
    for row in csvreader:
        #add all values from the first csv column to this list
        months.append(row[0])

        #to calculate the sum of the profit/losses column
        #a+=b means a=a+b, so for this application
        #runs through each row and adds value to the previous row.
        #total=total+next row
        total += int(row[1])

        #this formula is used to calculate the change values
        data=float(row[1])-prev_value
        prev_value=float(row[1])
        #each of the calculated change values is added to the list 'change_values'
        change_values.append(data)

        #IGNORE-I used this to find the min/max before I knew to calculate the change values
        #if float(row[1])>greatest_increase:
            #greatest_increase=float(row[1])
            #greatest_increase_month=str(row[0])

        #if float(row[1])<greatest_decrease:
            #greatest_decrease=float(row[1])
            #greatest_decrease_month=str(row[0])


#This line used to calculate the total number of months
numMonths=int(len(months))
#print(numMonths)
#print(total)

#This line used to calculate the average of the profit/losses column
average=round(total/numMonths,2)
#print(average)

#print(change_values)
#print(len(change_values))

#created a funtion that will return an average value of a list
#def Average(lst):
    #return sum(lst)/len(lst)

#first change_value is meaningless since the arbitraty prev_value is subtracted
#this line is used to remove the first value from the list
change_values.pop(0)
new_average=round(sum(change_values)/len(change_values),2)
#print(new_average)

#find the greatest increase in the change values using max function
greatest_increase=round(max(change_values),2)
#print(greatest_increase)

#find the greatest decrease in the change values suing the min function
greatest_decrease=min(change_values)
#print(greatest_decrease)

#find what index value is associated with the greatest_increase value so that
#we can return the month/year value from the list
greatest_increase_index=change_values.index(greatest_increase)
#print(greatest_increase_index)
#since the months list has an extra value(remember that we removed one from the change_values list)
#the month returned should be the greatest_increase_index plus one
#print(months[(greatest_increase_index)+1])


#print(change_values.index(greatest_decrease))
greatest_decrease_index=change_values.index(greatest_decrease)
#print(months[(greatest_decrease_index)+1])


#FINAL REPORT
print("Financial Analysis")
print("---------------------------")
print("Total Months:   "+str(numMonths))
#print(f'Total Months:  {numMonths}')
print("Total:   $"+str(total))
#print(f'Total:   ${total}')
print("Average Change:   $"+str(new_average))
#print(f'Average Change:   ${average}')
print('Greatest Increase in Profits:   '+str((months[(greatest_increase_index)+1]))+'   ($'+str(greatest_increase)+')')
print('Greatest Decrease in Profits:   '+str((months[(greatest_decrease_index)+1]))+'   ($'+str(greatest_decrease)+')')


txt_path=os.path.join('..','/Users/allysontalyor/Documents/Bootcamp_Assignments/python-challenge/PyBank','main.txt')

with open(txt_path,'w') as text_file:
    text_file.write("Financial Analysis\n---------------------------\nTotal Months:   86\nTotal:   $38382578\nAverage Change:   $-2315.12\nGreatest Increase in Profits:   Feb-2012   ($1926159.0)\nGreatest Decrease in Profits:   Sep-2013   ($-2196167.0)")
    
    



