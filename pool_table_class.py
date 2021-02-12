from datetime import datetime
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

    def current_time(self):
        return datetime() - self.start_time
    
    def cost_of_table(self):
        return 30 * self.end_time - self.start_time