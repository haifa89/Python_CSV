import os
import csv

#set path for the file 
path_csv = os.path.join('resources','budget_data.csv')

# open the Csv 
with open (path_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')

    # run over the header
    next(csv_reader)

    # make list for the data
    rows=list(csv_reader)
    number_of_rows = len(rows)

    total = 0
    # create dictionary
    changes_dict ={} 
    previous_value = int(rows[0][1])

    # loop through the rows to take a net total
    # loop through the rows to caculate the changes and append it to dictionary
    for row in rows:
        value = int(row[1])
        total += value
        change =value-previous_value
        changes_dict[change] = row[0] 
        previous_value =value 
    
    changes_sum = 0

    #loop through keys(because the value number in it) in dictionary to  take sum
    for number in changes_dict.keys():
        changes_sum += number
        
    # substruct from len by 1 because first month there is no change 
    average_change = changes_sum / (len(changes_dict)-1)
    

    #using round() method 
    average_change_round=(round(average_change,2))
   
    # find the greatest change increase 
    max_revenue_row = max(changes_dict.keys())

    # find the greatest change decrease 
    min_revenue_row = min(changes_dict.keys())

    # calling the name of dictionary and the key to take the value 
    max_number = (f"{changes_dict[max_revenue_row]} (${max_revenue_row}) ")
    min_number= (f"{changes_dict[min_revenue_row]} (${min_revenue_row})")

    #print to the terminal
    print("Financial Analysis")
    print("----------------------------------------------")
    print(f"Total Months: {number_of_rows}")
    print(f"Total: ${total} ")
    print(f"Average Change: ${average_change_round}")
    print(f"Greatest Increase in Profit: ${max_number}")
    print(f"Greatest Decrease in Profit: ${min_number}")

# Set variable for output file  
output_path = os.path.join('analysis',"output.txt")

# open the output file
with open(output_path,'w',newline="") as text_file:
    
    #write the results to text file 
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------------------------\n")
    text_file.write(f"Total Months: {number_of_rows}\n")
    text_file.write(f"Total: ${total} \n")
    text_file.write(f"Average Change: ${average_change_round}\n")
    text_file.write(f"Greatest Increase in Profit: ${max_number}\n")
    text_file.write(f"Greatest Decrease in Profit: ${min_number}\n")


    

    
    