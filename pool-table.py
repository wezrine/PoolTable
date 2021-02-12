from datetime import datetime
import json
tables = []
fmt = '%S'
from pool_table_class import PoolTable

def format_time(dt):
    if dt == None:
        return "Unoccupied"
    else:
        return dt.strftime(fmt)

def check_out_table():
    print("\nUNOCCUPIED TABLES:")
    for table in tables:
        if table.is_occupied == False:
            print(f"Table {table.number}")
    ask = int(input("\nChoose a table to check out: "))
    table = tables[ask-1]
    if table.is_occupied == True:
        print(f"Pool Table {table.number} is currently occupied")
    else:
        table.check_out()
        print(table.total_time())

def check_in_table():
    print("\nOCCUPIED TABLES:")
    for table in tables:
        if table.is_occupied == True:
            print(f"Table {table.number}")
    ask = int(input("\nChoose a table to check in: "))
    table = tables[ask-1]
    if table.is_occupied == False:
        print("Pool table was never occupied")
    else:
        table.check_in()
        print(f"\nTable {table.number} has been checked in. Total Time: ")
        print(format_time(table.start_time))
        print(format_time(table.end_time))
        print(table.total_time())

def view_all_tables():
    print("\nALL TABLES:")
    for table in tables:
        if table.is_occupied == False:
            print(f"Table {table.number}")
        else:
            # cost_of_table: unsupported operand type for * int and 
            print(f"Table {table.number} is currently occupied")

# creates 12 tables
for i in range (0,12):
    table = PoolTable(i+1)
    tables.append(table)

## MENU ##
while True:
    print("\nPOOL TABLE MANAGEMENT SYSTEM\n****************************\n")
    exit = input("Press [1] to check out a table\nPress [2] to check in a table\nPress [3] to view all tables\nPress any other key to quit\n\n")
    if exit == "1": # Check out a table
        check_out_table()
    elif exit == "2": # Check in a table
        check_in_table()
    elif exit == "3":
        view_all_tables()
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