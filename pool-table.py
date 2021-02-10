from datetime import datetime
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
        self.start_time = None
        self.is_occupied = False
    
    # def total_time(self):
    #     self.time_played = self.end_time - self.start_time

    # def total_time(self):
    #     self.time_played = datetime.now() - self.start_time

    # def time_clear(self):
    #     self.start_time = None

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
    ask = int(input("Choose a table: "))
    table = tables[ask-1]
    table.check_out()

def check_in_table():
    print("\nOCCUPIED TABLES:")

    for table in tables:
        if table.is_occupied == True:
            print(f"Table {table.number} | Start Time: {format_time(table.start_time)} | End Time: {format_time(table.end_time)} | Total Time Played: {format_time(table.time_played)}")
    ask = int(input("Choose a table: "))
    table = tables[ask-1]
    table.check_in()

# creates 12 tables
for i in range (0,12):
    table = PoolTable(i+1)
    tables.append(table)

## MENU ##
while True:
    print("\nPOOL TABLE MANAGEMENT SYSTEM\n****************************\n")
    exit = input("Press [1] to check out a table\nPress [2] to check in a table\n")
    if exit == "1":
        # Checkout a table
        check_out_table()
    elif exit == "2":
        # Checkin a table
        check_in_table()
