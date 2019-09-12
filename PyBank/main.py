import csv

total_months = 0
total_revenue = 0
average_change = 0
total_deleta_change_month_to_month = []
profit_increase_date = "Now"
profit_increase_revenue = 0
profit_decrease_date = "Now"
profit_decrease_revenue = 0

with open('02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv', newline='') as f:
    reader = csv.reader(f)
    # First row in the csv in the Column Name of Date and Profit
    # next will skip the Date and Column
    next(reader)

    # Need to look at previous row when calculating profit increase/decrease
    previous_row = None

    # Should be all the rows with actual data
    for row in reader:
        # Update total months
        total_months += 1

        # List get the first and last element
        current_date = row[0]
        current_revenue = int(row[-1])

        # Calculate Profit Increase & Decrease
        if profit_increase_date == "Now":
            #Increasing
            profit_increase_date = current_date
            profit_increase_revenue = current_revenue
            # Decreasing
            profit_decrease_date = current_date
            profit_decrease_revenue = current_revenue
        else:
            delta = current_revenue - int(previous_row[-1])

            # Need a list of all the changes from month to month
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
total = 0
for change in total_deleta_change_month_to_month:
    total += change

average_change = total / total_months

print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(total_months))
print('Total: $' + str(total_revenue))
print('Average Change: $' + str(average_change))
print('Greatest Increase in Profits: ' + profit_increase_date + " ($" + str(profit_increase_revenue) +")")
print('Greatest Decrease in Profits: ' + profit_decrease_date + " ($" + str(profit_decrease_revenue) +")")
