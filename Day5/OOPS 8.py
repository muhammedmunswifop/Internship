"""8. Hotel Room Booking System"""
class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_booked = False


class Guest:
    def __init__(self, name):
        self.name = name


class Booking:
    def book_room(self, room, guest):
        if room.is_booked:
            print(f"Room {room.room_number} is already booked.")
        else:
            room.is_booked = True
            print(f"Room {room.room_number} booked successfully for {guest.name}.")

    def cancel_booking(self, room):
        if not room.is_booked:
            print(f"Room {room.room_number} is not booked.")
        else:
            room.is_booked = False
            print(f"Booking for Room {room.room_number} has been cancelled.")

    def view_available_rooms(self, rooms):
        print("\nAvailable Rooms:")
        available = False
        for room in rooms:
            if not room.is_booked:
                print(f"Room {room.room_number}")
                available = True
        if not available:
            print("No rooms available.")


room1 = Room(101)
room2 = Room(102)
room3 = Room(103)

guest1 = Guest("Rahul")

booking = Booking()

rooms = [room1, room2, room3]

booking.view_available_rooms(rooms)

booking.book_room(room1, guest1)
booking.book_room(room1, guest1)  

booking.view_available_rooms(rooms)

booking.cancel_booking(room1)

booking.view_available_rooms(rooms)