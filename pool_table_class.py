from datetime import datetime

class PoolTable:
    def __init__(self,number):
        self.number = number
        self.is_occupied = False
        self.start_time = None
        self.end_time = None
        self.time_played = None
        self.cost = 0.00

    def current_time(self):
        return datetime.now() - self.start_time

    def check_out(self):
        self.is_occupied = True
        self.start_time = datetime.now()
        self.end_time = None
        self.cost = 1.00
        
    def check_in(self):
        self.is_occupied = False
        self.end_time = datetime.now()
        self.time_played = self.current_time()
        self.cost += 30*(self.current_time().total_seconds())/3600

    def view_tables(self):
        self.end_time = self.current_time()
        self.time_played = self.current_time()
        self.cost += 30*(self.current_time().total_seconds())/3600

    def clear(self):
        self.end_time = None
        self.time_played = None
        self.cost = 1.00