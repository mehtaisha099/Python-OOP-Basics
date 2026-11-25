class Flight:
    def __init__(self, flight_number, total_seats):
        self.flight_number = flight_number
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print("Seat booked successfully")
        else:
            print("No seats available")

    def show_seats(self):
        print("Available seats:", self.total_seats - self.booked_seats)


flight = Flight("AI101", 3)

flight.show_seats()
flight.book_seat()
flight.book_seat()
flight.show_seats()