# This is PyBank 
import os  
import csv

budget_data_csv = os.path.join('..','Resources_PyBank', 'budget_data.csv')

print("Financial Analysis")
print("---------------------------------------")


profits = []
months = []
profit = 0
month = 0

def bank_data (budget_data):

    months = budget_data[0]
    profits = budget_data[1]
    return (months,profits)

with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader: 
        #find number of months 
        month, raw_profit = bank_data(row)
        months.append(month)
        profits.append(profit)
        profit += int(raw_profit)
    print(f'Number of months: {len(months)}')

    print(f'Total Sum: {profit}')
    
    change = []
    #find avg change
    for i in range (1, len(profits)):
        diff = profits[i] - profits[i-1]
        change.append(diff)
        mndiff = diff / len(profits)
    print(f'Average Change: {mndiff}')

    #greatest increase in profits
    maxp = max(change)
    minp = min(change)

    print(f'Greatest Increase in Profits: {maxp}')
    print(f'Greatest Decrease in Profits: {minp}')

open("PyBank", "w+")