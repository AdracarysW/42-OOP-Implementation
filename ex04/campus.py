class Campus:

    def __init__(self):
        self.buildings = []
        self.num_buildings = 0
        self.total_capacity = 0

    def get_info(self):
        print("The campus has {} building(s) with a combined capacity of {} people".format(self.num_buildings, self.total_capacity))

    def add_building(self, b):
        self.buildings.append(b)
        self.num_buildings += 1
        self.total_capacity += b.capacity
