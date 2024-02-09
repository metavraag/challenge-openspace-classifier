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

    def report(self):
        total_tables = len(self.tables)
        seats_per_table = [len(table.seats) for table in self.tables]
        total_seats = sum(seats_per_table)
        occupied_seats = sum(not seat.free for table in self.tables for seat in table.seats)
        free_seats = total_seats - occupied_seats
        waiting_list_length = len(self.waiting_list)

        # General report
        print("Openspace Configuration Report:")
        print(f"There are a total of {total_tables} tables with an overall seating capacity of {total_seats} seats.")
        
        if all(seat_count == seats_per_table[0] for seat_count in seats_per_table):
            print(f"Each table has {seats_per_table[0]} seats.")
        else:
            seat_counts = ", ".join(str(count) for count in seats_per_table)
            print(f"Tables have varying seat capacities: {seat_counts}.")
        
        print(f"Currently, {occupied_seats} seats are occupied and {free_seats} seats remain available.")

        # Waiting list report with names
        if waiting_list_length > 0:
            waiting_names = ", ".join(self.waiting_list)
            print(f"There are {waiting_list_length} people waiting for a seat: {waiting_names}.")
        else:
            print("There is no one on the waiting list at the moment.")