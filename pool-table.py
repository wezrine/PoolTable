tables = []
from datetime import datetime

class PoolTable:
    def __init__(self,number):
        self.number = number
        self.is_occupied = False
        self.start_time = None
        self.end_time = None
        self.total_time = None

    def checkout(self):
        self.start_time = datetime.now()
        self.end_time = None
        self.is_occupied = True
    
    def checkin(self):
        self.end_time = datetime.now()
        self.start_time = None
        self.is_occupied = False
    
def check_out_table():
    print("\nUNOCCUPIED TABLES:")
    for table in tables:
        if table.is_occupied == False:
            print(f"Table {table.number}")
    ask = int(input("Choose a table: "))
    table = tables[ask-1]
    table.checkout()

def check_in_table():
    print("\nOCCUPIED TABLES:")
    for table in tables:
        if table.is_occupied == True:
            print(f"Table {table.number}")
    ask = int(input("Choose a table: "))
    table = tables[ask-1]
    table.checkin()

# creates 12 tables
for i in range (0,12):
    table = PoolTable(i+1)
    tables.append(table)

## MENU ##
while True:
    exit = input("\nPOOL TABLE MANAGEMENT SYSTEM\n****************************\nPress [1] to check out a table\nPress [2] to check in a table\n")
    if exit == "1":
        # Checkout a table
        check_out_table()
    elif exit == "2":
        # Checkin a table
        check_in_table()
