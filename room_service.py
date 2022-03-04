"""
This program is ...
Created by ...
"""

guests = {'102':'Peter', '103':'Peter', '105':'Mary', '107':'Daniel'}

def check_guest(name, room):
    msg = None
    if room in guests.keys():
        if guests[room] == name:
            msg = 'Welcome!'
        else:
            msg = "Your info doesn't match out records"
    else:
        msg = f"Room {room} hasn't been booked."
    return msg


name = input("What's your name? ")
room = input("What's your room number? ")

print (check_guest(name, room))