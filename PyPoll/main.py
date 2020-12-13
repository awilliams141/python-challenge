import os
import csv

# defining csv path
csvpath = os.path.join('Resources', 'election_data.csv')

# opening csv
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    total = 0
    khanVotes = 0
    correyVotes = 0
    liVotes = 0
    otoolVotes = 0

    # looping through items in csv
    for row in csvreader:
        total += 1
        if row[2] == "Khan":
            khanVotes += 1
        elif row[2] == "Correy":
            correyVotes += 1
        elif row[2] == "Li":
            liVotes += 1
        elif row[2] == "O'Tooley":
            otoolVotes += 1

        # determing who received the most votes
        if khanVotes > correyVotes and khanVotes > liVotes and khanVotes > otoolVotes:
            winner = "Khan"
        elif correyVotes > khanVotes and correyVotes > liVotes and correyVotes > otoolVotes:
            winner = "Correy"
        elif liVotes > khanVotes and liVotes > correyVotes and liVotes > otoolVotes:
            winner = "Li"
        elif otoolVotes > khanVotes and otoolVotes > correyVotes and otoolVotes > liVotes:
            winner = "O'Tooley"

    # calculating percent of votes won
    khanPer = (khanVotes / total) * 100
    correyPer = (correyVotes / total) * 100
    liPer = (liVotes / total) * 100
    otoolPer = (otoolVotes / total) * 100
    
    # printing results to the console
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total}")
    print("-------------------------")
    print(f"Khan: {round(khanPer, 3)}% ({khanVotes})")
    print(f"Correy: {round(correyPer, 3)}% ({correyVotes})")
    print(f"Li: {round(liPer, 3)}% ({liVotes})")
    print(f"O'Tooley: {round(otoolPer, 3)}% ({otoolVotes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")   

# define output path
output_path = os.path.join("Analysis", "PyPoll.txt")

# Opening the file and writing the output
with open(output_path, 'w', newline='') as txtfile:
    
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Khan: {round(khanPer, 3)}% ({khanVotes})\n")
    txtfile.write(f"Correy: {round(correyPer, 3)}% ({correyVotes})\n")
    txtfile.write(f"Li: {round(liPer, 3)}% ({liVotes})\n")
    txtfile.write(f"O'Tooley: {round(otoolPer, 3)}% ({otoolVotes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")  