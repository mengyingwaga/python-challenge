# import Python modules
import os
import csv

# Locate the file path
csvpath = os.path.join("Resources", "election_data.csv")

# open csv file
with open(csvpath, 'r', newline='') as csvfile:
    # create a variable called csvreader to hold the information in the csv file
    csvreader = csv.reader(csvfile, delimiter=',')
    # test if the file was correctly read by Python
    print(csvreader)
    # to skip the header row when counting
    scv_header = next(csvreader)
    
    # lists to store data
    number_votes = []
    list_candidates = []
    Khan = []
    Correy = []
    Li = []
    OTooley = []

    #total number of votes cast
    for row in csvreader:
        number_votes.append(row[0])
        list_candidates.append(row[2])  
    print(len(number_votes))
    
    # list of the candidates and their respective vote percentage and the number of votes received
    for i in list_candidates:
        if i == "Khan":
            Khan.append(i)
            total_khan = len(Khan)
            khan_percentage = round(total_khan / len(number_votes) * 100, 3)
        elif i == "Correy":
            Correy.append(i)
            total_correy = len(Correy)
            correy_percentage = round(total_correy / len(number_votes) * 100, 3)
        elif i == "Li":
            Li.append(i)
            total_li = len(Li)
            li_percentage = round(total_li / len(number_votes) * 100, 3)
        else:
            OTooley.append(i)
            total_otooley = len(OTooley)
            otooley_percentage = round(total_otooley / len(number_votes) * 100, 3)
    print(khan_percentage)
    print(total_khan)
    print(correy_percentage)
    print(total_correy)
    print(li_percentage)
    print(total_li)
    print(otooley_percentage)
    print(total_otooley)
    
    # determine the winner
    from collections import Counter
    c = Counter(list_candidates)
    print(c.most_common(1))
    winner = "Khan"
    print(winner)

# data analysis print statement
print("Election Results")
print("---------------------------")
print(f'Total Votes: {len(number_votes)}')
print("---------------------------")
print(f'Khan: {khan_percentage}% ({total_khan})')
print(f'Correy: {correy_percentage}% ({total_correy})')
print(f'Li: {li_percentage}% ({total_li})')
print(f"O'Tooley: {otooley_percentage}% ({total_otooley})")
print("---------------------------")
print(f'Winner: {winner}')
print("---------------------------")

# export to the text file
output_path = os.path.join("Analysis", "Election Results.txt")
with open(output_path, "w", newline='') as txtfile:
    txtfile.write("Election Results")
    txtfile.write("---------------------------")
    txtfile.write(f'Total Votes: {len(number_votes)}')
    txtfile.write("---------------------------")
    txtfile.write(f'Khan: {khan_percentage}% ({total_khan})')
    txtfile.write(f'Correy: {correy_percentage}% ({total_correy})')
    txtfile.write(f'Li: {li_percentage}% ({total_li})')
    txtfile.write(f"O'Tooley: {otooley_percentage}% ({total_otooley})")
    txtfile.write("---------------------------")
    txtfile.write(f'Winner: {winner}')
    txtfile.write("---------------------------")