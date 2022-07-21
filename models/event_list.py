from models.event import Event

event1 = Event("21/07/2022", "Meet Up", 10, "Glasgow", "Lean Coffee")
event2 = Event("02/05/2022", "Meeting", 20, "Edinburgh", "Lunch")
event3 = Event("08/06/2022", "Coffe Morning", 8, "Roma", "Breakfast")

events = [event1, event2, event3]


def add_event(event):
    events.append(event)