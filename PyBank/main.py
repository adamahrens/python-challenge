import csv

total_months = 0
total_revenue = 0
average_change = 0
total_deleta_change_month_to_month = []
profit_increase_date = ""
profit_increase_revenue = 0
profit_decrease_date = ""
profit_decrease_revenue = 0

with open('02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv', newline='') as f:
    reader = csv.reader(f)
    # First row in the csv in the Column Name of Date and Profit next will skip the Date and Column
    next(reader)

    # Need to look at previous row when calculating profit increase/decrease
    previous_row = []

    for row in reader:
        total_months += 1

        # row is a List get the first (Date) and last (Revenue) element
        current_date = row[0]
        current_revenue = int(row[-1]) # Casting from a String to Integer

        # Calculate Profit Increase & Decrease
        # Since its the first row of data
        # we need to to set the default values
        # we have nothing else to compare it to.
        if len(profit_increase_date) == 0:
            #Increasing
            profit_increase_date = current_date
            profit_increase_revenue = current_revenue
            # Decreasing
            profit_decrease_date = current_date
            profit_decrease_revenue = current_revenue
        else:
            # Whats the change from this month to the previous
            delta = current_revenue - int(previous_row[-1])
            total_deleta_change_month_to_month.append(delta)

            # Is it a big profit?
            if delta > profit_increase_revenue:
                profit_increase_revenue = delta
                profit_increase_date = current_date

            # Is it a big loss?
            if delta < profit_decrease_revenue:
                profit_decrease_revenue = delta
                profit_decrease_date = current_date

        # Update total_revenue
        total_revenue += current_revenue

        # Update the previous rows
        previous_row = row

# Calculate average change from month to month
average_change = sum(total_deleta_change_month_to_month) / len(total_deleta_change_month_to_month)

print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(total_months))
print('Total: $' + str(total_revenue))
print('Average Change: $' + str(average_change))
print('Greatest Increase in Profits: ' + profit_increase_date + " ($" + str(profit_increase_revenue) +")")
print('Greatest Decrease in Profits: ' + profit_decrease_date + " ($" + str(profit_decrease_revenue) +")")

# Write to file
file = open('financial-analysis.txt', 'a')
file.write('Financial Analysis')
file.write('\n')
file.write('----------------------------')
file.write('\n')
file.write('Total Months: ' + str(total_months))
file.write('\n')
file.write('Average Change: $' + str(average_change))
file.write('\n')
file.write('Greatest Increase in Profits: ' + profit_increase_date + " ($" + str(profit_increase_revenue) +")")
file.write('\n')
file.write('Greatest Decrease in Profits: ' + profit_decrease_date + " ($" + str(profit_decrease_revenue) +")")
file.close()
