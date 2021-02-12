# Assignment - Pool Table Project

The goal of this project was to create a pool table management app which will manage the pool tables in a university games room.

# Requested Features:

- Admin should be able to see all tables (12)
- Should show whether table is OCCUPIED or NOT OCCUPIED
- If table is occupied, show the start time, total time, cost
- Admin can only give out tables that are NOT OCCUPIED, if table is OCCUPIED the app will print a message saying "Pool Table 8 is currently occupied"
- App prints data to .txt and .json

# My App:

My app allows the user to either 
  (1) check out the table
  (2) check in the table
  (3) view all tables
  
When (1) is selected, the app displays all unoccupied pool tables and asks the admin to select one to check out. If the admin inputs a table that is occupied, it will prompt the admin that he or she cannot check out a occupied table. When the table is selected, its start_time is logged. There is a minimum fee of $ 1.00.

When (2) is selected, the app displays all occupied pool tables and asks for selection. Similar to (1), unoccupied tables cannot be checked in. At the time of checkout, a tables's total time is logged and shows the admin the total cost.

When (3) is selected, all tables with occupancy display the number, start time, total time played and cost. 


Currently the app is in working condition. I would like to format the time in a more efficient and user-friendly way. Also, the app could be improved by importing the file beforehand, so that it can act as a working database.
