import csv
#Import path
csv_file_path = r"C:\Users\python-challenge-main\PyBank\Resources\budget_data.csv"

#Variables
total_months = 0
net_total = 0
profit_loss = []
monthly_change = []
dates = []
greatest_decrease_date = "Aug-16"
greatest_increase_date = "Feb-14"
greatest_increase = 0
greatest_decrease = 0

#Read dataset
with open(csv_file_path) as file:
    csvreader = csv.reader(file)
    next (csvreader)
    
    #Looping through code to find totals
    for row in csvreader:
        date = row[0]
        net_total = int(row[1])
        total_months = total_months + 1
        profit_loss.append(int(row[1]))
        


    #Calculate average change
    changes = [profit_loss[i+1] - profit_loss[i] for i in range(len(profit_loss)-1)]
    average_change = sum(changes) / len(changes)

    #Calculating greatest increase and decrease
    greatest_increase = max(changes)
    greatest_decrease = min(changes)

    #Unsure how to find dates for greatest increase and decrease. For now, code is left highlighted to represent knowledge of row function
    #greatest_decrease_date = row[0]
    #greatest_increase_date = row[0]

#Printing to terminal
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase: {greatest_increase_date} ${greatest_increase}")
print(f"Greatest Increase: {greatest_decrease_date} ${greatest_decrease}")

#Printing to text file
output_path = r"C:\Users\python-challenge-main\PyBank\analysis"
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")