
class Seat:
    def __init__(self):
        self.free = True
        self.occupant = None

    def __str__(self) -> str:
        """
        Return a string representation of the seat, showing if it's occupied or free.

        :return: A string indicating the seat's occupancy status.
        """
        return self.occupant if self.occupant else "Free"

    def set_occupant(self, name):
        """Assigns an occupant to the seat if it's free."""
        if self.free:
            self.occupant = name
            self.free = False
            return f"{name} has been assigned to the seat."
        else:
            return "The seat is already occupied."

    def remove_occupant(self):
        """Removes the occupant from the seat and returns the name of the occupant."""
        if self.free:
            return "The seat is already free."
        else:
            occupant_name = self.occupant
            self.occupant = None
            self.free = True
            return f"{occupant_name} has been removed from the seat."

    def to_dict(self):
        return {
            'occupant': self.occupant,
            'free': self.free
        }


class Table:
    def __init__(self, capacity):
        """
        Initializes a Table object with the given capacity.

        :param capacity (int): The maximum number of seats at the table.

        """
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def __str__(self) -> str:
        """
        Provide a string representation of the table, including its name and occupants.

        :return: A string describing the table and its occupants.
        """
        occupants = ', '.join(str(seat) for seat in self.seats)
        return f"Table {self.name}: {occupants}"

    def has_free_spot(self):
        """Checks if there is at least one free spot at the table."""
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name):
        """Assigns a seat to a person with the given name if a free spot is available."""
        for seat in self.seats:
            if seat.free:
                return seat.set_occupant(name)
        return "No free spots available at the table."

    def left_capacity(self):
        """Returns the number of free spots available at the table."""
        return sum(seat.free for seat in self.seats)

    def to_dict(self):
        """
        Converts the Table object to a dictionary.

        Returns:
            dict: A dictionary representation of the Table object.
        """
        return {
            'seats': [seat.to_dict() for seat in self.seats]
        }

