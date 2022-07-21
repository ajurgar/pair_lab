from flask import render_template, request, redirect
from app import app
from models.event import *
from models.event_list import *

@app.route('/events')
def index():
    return render_template("events/index.html", title = "Home", all_events = events)

@app.route('/events/new')
def new():
    return render_template("events/new.html", title="Add New Event")

@app.route('/events', methods=["POST"])
def create():

    event_date = request.form["event_date"]
    name_event = request.form["name_event"]
    number_guests = request.form["number_guests"]
    room = request.form["room"]
    description = request.form["description"]
    new_event = Event(event_date, name_event, number_guests, room, description)
    add_event(new_event)
    return redirect("/events")

