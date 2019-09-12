import csv

total_months = 0
total_revenue = 0
average_change = 0
profit_increase_date = "Now"
profit_increase_revenue = 0
profit_decrease_date = "Now"
profit_decrease_revenue = 0

# First row in the csv in the Column Name of Date and Profit
with open('02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv', newline='') as f:
    reader = csv.reader(f)
    # next will skip the Date and Column
    next(reader)

    # Should be all the rows with actual data
    for row in reader:
        # Update total months
        total_months += 1

        # List get the first and last element
        current_date = row[0]
        current_revenue = row[-1]

        # Update total_revenue
        total_revenue += int(current_revenue)

print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(total_months))
print('Total: $' + str(total_revenue))
print('Average Change: $' + str(average_change))
print('Greatest Increase in Profits: ' + profit_increase_date + " ($" + str(profit_increase_revenue) +")")
print('Greatest Decrease in Profits: ' + profit_decrease_date + " ($" + str(profit_decrease_revenue) +")")
