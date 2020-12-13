import os
import csv

# declaring csv path
csvpath = os.path.join('Resources', 'budget_data.csv')

# opening csv file 
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

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
        
    # printing the analysis to the console
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round((average / months), 2)}")
    print(f"Greatest Increase in Profits: {increaseDate} (${increase})")
    print(f"Greatest Decrease in Profits: {decreaseDate} (${decrease})")

# define output path
output_path = os.path.join("Analysis", "PyBank.txt")

# Opening the file and writing the output
with open(output_path, 'w', newline='') as txtfile:
    
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {months}\n")
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change: ${round((average / months), 2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {increaseDate} (${increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {decreaseDate} (${decrease})\n")