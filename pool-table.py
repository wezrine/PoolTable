from datetime import datetime
import json
tables = []
fmt = '%H:%M:%S'

class PoolTable:
    def __init__(self,number):
        self.number = number
        self.is_occupied = False
        self.start_time = None
        self.end_time = None
        self.time_played = None

    def check_out(self):
        self.start_time = datetime.now()
        self.end_time = None
        self.is_occupied = True
    
    def check_in(self):
        self.end_time = datetime.now()
        self.is_occupied = False
    
    def total_time(self):
        return self.end_time - self.start_time

def format_time(dt):
    if dt == None:
        return "Time not started"
    else:
        return dt.strftime(fmt)

def check_out_table():
    print("\nUNOCCUPIED TABLES:")
    for table in tables:
        if table.is_occupied == False:
            print(f"Table {table.number}")
    ask = int(input("\nChoose a table: "))
    table = tables[ask-1]
    table.check_out()

def check_in_table():
    print("\nOCCUPIED TABLES:")
    for table in tables:
        if table.is_occupied == True:
            print(f"Table {table.number}")
    ask = int(input("\nChoose a table: "))
    table = tables[ask-1]
    table.check_in()
    print(f"Table {table.number} - Total Time: {table.total_time()}")

# creates 12 tables
for i in range (0,12):
    table = PoolTable(i+1)
    tables.append(table)

## MENU ##
while True:
    print("\nPOOL TABLE MANAGEMENT SYSTEM\n****************************\n")
    exit = input("Press [1] to check out a table\nPress [2] to check in a table\nPress any other key to quit\n\n")
    if exit == "1": # Check out a table
        check_out_table()
    elif exit == "2": # Check in a table
        check_in_table()
    else:
        break

# Writes to txt
with open("11-22-2017.txt","w") as file:
    for pt in tables:
        table_info = f"#{pt.number} - START: {format_time(pt.start_time)} - END: {format_time(pt.end_time)}\n"
        file.write(table_info)

# Writes to JSON
array = []
with open("11-22-2017.json","w") as file_object:
    for table in tables:
        user = {"TableNo": table.number, "Start": format_time(table.start_time), "End": format_time(table.end_time)}
        array.append(user)
    json.dump(array,file_object)
    



