import random
from table import Table 

class Openspace:
    def __init__(self, number_of_tables, capacity_per_table):
        self.number_of_tables = number_of_tables
        self.tables = [Table(capacity_per_table) for _ in range(number_of_tables)]

    def organize(self, names):
        """Randomly assigns people to seats in various tables."""
        shuffled_names = random.sample(names, len(names))
        for name in shuffled_names:
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

    def store(self, filename):
        """Stores the seating arrangement in an file."""
        pass
