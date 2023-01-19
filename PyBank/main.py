# import required modules to read csv
import os
import csv

# create variables for list set up
row_count = 0
months = []
total = 0
profit = []
change = 0
change_in_profit = []
largest_increase = 0
largest_decrease = 0
month_largest_decrease = ''
month_largest_increase = ''

# read in csv file
csvpath = os.path.join('.','Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read the header row in first
    csv_header = next(csvreader)

    for row in csvreader:
        # set row counter for csv file read in
        row_count += 1

        # determine number of months in csv budget file, write to months list
        months.append(row[0])

        # convert P&L to integer, create net P&L measure
        total += int(row[1])

        # convert month profit to integer, write to list
        profit.append(int(row[1]))

    # use for loop to determine profit. profit is diffrence between current row and row above, 
    # use conditional logic to handle change when i =0.. since 0-1 = -1 --> profit from last row in dataset
    for i in range(len(profit)):
        if i == 0:
            change = 0
        else:
            change = int(profit[i]) - int(profit[i-1])
            if (change >= largest_increase):
                month_largest_increase = months[i]
                largest_increase = change
            if (change <= largest_decrease):
                month_largest_decrease = months[i]
                largest_decrease = change
        
        change_in_profit.append(change)

    average_change = round(sum(change_in_profit) / (len(change_in_profit)-1),2)

print(" Financial Analysis")
print("-" * 25)
print(f"Total Months: {row_count}") 
print("Total: $" + str(total))
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {month_largest_increase} (${largest_increase})")
print(f"Greatest Decrease in Profits: {month_largest_decrease} (${largest_decrease})")

# write summary of analysis to text file
output_file = os.path.join('.','Analysis', 'Financial_Analysis.txt')
with open(output_file, 'w', newline='') as text:
    text.write(" Financial Analysis\n")
    text.write("-----------------------\n")
    text.write(f"Total Number of Months: {row_count}\n")
    text.write(f"Total $ {total}\n")
    text.write(f'Average Change in P&L $ {average_change}\n')
    text.write(f'Greatest Increase in Profit: {month_largest_increase} (${largest_increase}')
    text.write(f'Greatest Decrease in Profit: {month_largest_decrease} (${largest_decrease}')    

