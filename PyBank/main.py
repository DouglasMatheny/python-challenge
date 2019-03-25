import os
import csv

#Declare and initialize variables
budgetdata_csv_path = os.path.join("Resources", "budget_data.csv")
results_path = os.path.join("Resources", "results.txt")
x_max_amt = float('-inf')
x_min_amt = float('+inf')
x_max_mon = ""
x_min_mon = ""
total_months =  int(0)
total =  float(0)

#Read in the file and set values.
with open(budgetdata_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        if float(row[1]) < x_min_amt:
            x_min_amt = float(row[1])
            x_min_mon = str(row[0])
        if float(row[1]) > x_max_amt:
            x_max_amt = float(row[1])
            x_max_mon = str(row[0])
        total_months = total_months +1
        total = total + float(row[1])

#Put the results in a dictionary.
results = {}
results["Total Months:"] =  total_months
results["Total:"] =  "$"+str(int(total))
results["Average  Change:"] = "$"+str(round((total/total_months),2))
results["Greatest Increase in Profits:"] = [x_max_mon, "($"+str(int(x_max_amt))+")"]
results["Greatest Decrease in Profits:"] = [x_min_mon, "($"+str(int(x_min_amt))+")"]

#Print and save the results
with open(results_path,"w") as f:
     for key in results:
         f.write(f"{key} {results[key]}\n")
         print(f"{key} {results[key]}")
