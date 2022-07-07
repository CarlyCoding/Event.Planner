from asyncio import events
from cmath import e
from crypt import methods
from flask import render_template, request, redirect
from app import app
from models.list_of_events import events, add_new_event
from models.event import Event


@app.route('/events')
def index():
    return render_template('index.html', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['event-name']
    event_guests = request.form['no-guests']
    event_location = request.form['room-location']
    event_description = request.form['description']
    new_event = Event(event_date, event_name, event_guests, event_location, event_description)
    add_new_event(new_event)
    return redirect('/events')