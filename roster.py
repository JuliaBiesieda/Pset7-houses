import sys
from cs50 import SQL

db = SQL("sqlite:///students.db")

# check if user provided 2 command-line arguments
if len(sys.argv) != 2:
    print(f"Usage: python roster.py house_name")
    exit(0)

# select the students of the house specified by user and order by last name
data = db.execute("SELECT * FROM students WHERE house = (?) ORDER BY last", sys.argv[1])
# print(data)

# iterate through all the students in data
for student in data:

    # if the student has middle name print it
    if student["middle"] != None:
        print("{} {} {}, born {}".format(student['first'], student['middle'], student['last'], student['birth']))

    # if the student has no middle name, skip it
    else:
        print("{} {}, born {}".format(student['first'], student['last'], student['birth']))
