# import budget_data.csv
import os
import csv

# set path for file
csvpath = os.path.join("Resources", "Budget_data.csv")

# lists to store data
months = []
total_profit_loss = []
profit_loss_change = []

# open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # remove the header line when counting
    csv_header = next(csvreader)
    
    # total months number
    for row in csvreader:
        months.append(row[0])  
    #net total amount of profit and loss for entire period
        total_profit_loss.append(int(row[1]))
    print(len(months))
    print(round(sum(total_profit_loss)), )

    # change in profits by date and amount
    i = 0
    for i in range(len(total_profit_loss) - 1):
        profit_loss = int(total_profit_loss[i+1]) - int(total_profit_loss[i])
        profit_loss_change.append(profit_loss)
        total = sum(profit_loss_change)
        Average_profit_loss_change = total / len(profit_loss_change)
    print(round(Average_profit_loss_change, 2))

    # greatest increase in profits by amount and date
    greatest_increase = max(profit_loss_change)
    print(round(greatest_increase, 2))
    j = profit_loss_change.index(greatest_increase) + 1
    date_greatest_increase = months[j]
    print(date_greatest_increase)

    # greatest decrease in profits by amount and date
    greatest_decrease = min(profit_loss_change)
    print(round(greatest_decrease, 2))
    k = profit_loss_change.index(greatest_decrease) + 1
    date_greatest_decrease = months[k]
    print(date_greatest_decrease)

# data analysis print statement
print("Financial Analysis")
print("------------------------------")
print(f'Total months: {len(months)}')
print(f'Total: ${round(sum(total_profit_loss))}')
print(f'Average Change: ${round(Average_profit_loss_change, 2)}')
print(f'Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})')

#export to the text file
output_path = os.path.join("Analysis", "Financial Analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write("----------------------------------")
    txtfile.write(f'Total months: {len(months)}')
    txtfile.write(f'Total: ${round(sum(total_profit_loss))}')
    txtfile.write(f'Average Change: ${round(Average_profit_loss_change, 2)}')
    txtfile.write(f'Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})')
    txtfile.write(f'Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})')