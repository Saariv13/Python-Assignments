import csv

# Initialize dictionaries to store total and highest marks
total_marks = {}
highest_marks = {}
t = input("Enter the person you want to see? ").lower()
# Read the CSV file
with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        student_name = row['Student Name'].lower()
        marks = float(row['Mark'])

        # Calculate total marks
        if student_name in total_marks:
            total_marks[student_name] += marks
        else:
            total_marks[student_name] = marks

        # Calculate highest marks
        if student_name in highest_marks:
            highest_marks[student_name] = max(highest_marks[student_name], marks)
        else:
            highest_marks[student_name] = marks

# Print the dictionaries
print("Total Marks:", total_marks)
print("Highest Marks:", highest_marks)
#For bonus
print("Total Marks for " + t + " is " + str(total_marks.get(t)))
print("Highest Marks for " + t + " is " + str(highest_marks.get(t)))
'''
#def load_data(filename): 
    mylist =
    with open(filename) as marks:#Opens data
        students_data = csv.reader(students, delimiter=',') #<-- tells it is csv file and sets marks
        next(students_data) #Skips the header
        for row in students_data:#loops through our data
            mylist.append(row)
        return mylist

new_list = load_data('students.csv.xlsx')
for row in new_list:
    print(row)
'''