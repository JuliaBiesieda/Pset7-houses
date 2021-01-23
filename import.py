import csv
from cs50 import SQL
import sys
import json

db = SQL("sqlite:///students.db")

# check the num of command-line arguments
if len(sys.argv) != 2:
    print("Usage: python import.py filename.csv")
    exit(0)

# open the csv file given by com-line arg using csv reader
with open(sys.argv[1], "r") as csv_names:
    dict_reader = csv.DictReader(csv_names)
    list_of_dict = list(dict_reader)
    list_of_dict = json.loads(json.dumps(list_of_dict))

    # for each row, parse names
    for row in list_of_dict:
        name = row['name'].split()
        if len(name) != 3:
            name.insert(1, None)

        # insert each student into the table
        house = row['house']
        birth = row['birth']

        first_n = name[0]
        middle_n = name[1]
        last_n = name[2]

        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                   first_n, middle_n, last_n, house, birth)