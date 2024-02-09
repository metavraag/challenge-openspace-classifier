import random
from .table import Table 
import json

class Openspace:
    def __init__(self, number_of_tables, capacity_per_table):
        self.number_of_tables = number_of_tables
        self.tables = [Table(capacity_per_table) for _ in range(number_of_tables)]
        self.total_capacity = number_of_tables * capacity_per_table
        self.waiting_list = []

    def organize(self, names):
        """Randomly assigns people to seats in various tables."""
        shuffled_names = random.sample(names, len(names))
        seating_list = shuffled_names[:self.total_capacity] 
        self.waiting_list = shuffled_names[self.total_capacity:]
        for name in seating_list:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break

    def display(self):
        """Displays the tables and their occupants in a readable format."""
        for i, table in enumerate(self.tables, start=1):
            print(f"Table {i}:")
            for seat in table.seats:
                status = seat.occupant if seat.occupant else "Free"
                print(f"  - {status}")

    def store(self, filename="seating.json"):
        """Stores the seating arrangement in an file."""
        state = {
            'tables': [{'name': f"Table{i+1}", 'seats': table.to_dict()['seats']} for i, table in enumerate(self.tables)],
            # 'tables': [table.to_dict() for table in self.tables],
                  'waiting_list': self.waiting_list}
        with open(filename, 'w') as f:
            json.dump(state, f, indent=4)

        # pass
