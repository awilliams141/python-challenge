import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    months = 0
    total = 0
    last = 867884
    average = 0
    increase = 0
    decrease = 0
    
    for row in csvreader:
        months += 1
        total += int(row[1]) 
        average += (int(row[1]) - last)
        last = int(row[1])
        if int(row[1]) > int(increase):
            increase = row[1]
            increaseDate = row[0]
        if int(row[1]) < int(decrease):
            decrease = row[1]
            decreaseDate = row[0]
        
        #decrease += min(row[1])

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round((average / months), 2)}")
    print(f"Greatest Increase in Profits: {increaseDate} (${increase})")
    print(f"Greatest Decrease in Profits: {decreaseDate} (${decrease})")

        