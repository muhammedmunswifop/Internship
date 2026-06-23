"""9. Movie Ticket Booking System"""
class Movie:
    def __init__(self, title):
        self.title = title


class Theater:
    def __init__(self, name, total_seats):
        self.name = name
        self.seats = {}

        for seat_no in range(1, total_seats + 1):
            self.seats[seat_no] = False  


class Ticket:
    def __init__(self, movie, theater):
        self.movie = movie
        self.theater = theater

    def book_seat(self, seat_no):
        if seat_no not in self.theater.seats:
            print("Invalid seat number.")
        elif self.theater.seats[seat_no]:
            print(f"Seat {seat_no} is already booked.")
        else:
            self.theater.seats[seat_no] = True
            print(f"Seat {seat_no} booked successfully.")

    def cancel_booking(self, seat_no):
        if seat_no not in self.theater.seats:
            print("Invalid seat number.")
        elif not self.theater.seats[seat_no]:
            print(f"Seat {seat_no} is not booked.")
        else:
            self.theater.seats[seat_no] = False
            print(f"Booking for Seat {seat_no} cancelled.")

    def display_available_seats(self):
        print("\nAvailable Seats:")
        available = [seat for seat, booked in self.theater.seats.items()
                     if not booked]

        if available:
            print(*available)
        else:
            print("No seats available.")


movie = Movie("Avengers")
theater = Theater("PVR Cinema", 10)

ticket = Ticket(movie, theater)

ticket.display_available_seats()

ticket.book_seat(3)
ticket.book_seat(5)
ticket.book_seat(3)  

ticket.display_available_seats()

ticket.cancel_booking(3)

ticket.display_available_seats()
