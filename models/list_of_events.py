from models.event import Event

event1 = Event("03/03/2022", "Birthday Party", 1, "Meeting Room 1", "A lonely, lonely time")
event2 = Event("05/06/2022", "First Date", 2, "Park", "Love is in the air")
event3 = Event("10/02/2022", "Wedding", 50, "Edinburgh Castle", "Happily ever after")
events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)