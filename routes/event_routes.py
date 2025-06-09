from flask import Blueprint, request, jsonify
from models import Event
from app import db
from datetime import datetime
import pytz

event_bp = Blueprint('events', __name__)


@event_bp.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    try:
        ist = pytz.timezone("Asia/Kolkata")
        start = ist.localize(datetime.fromisoformat(data["start_time"]))
        end = ist.localize(datetime.fromisoformat(data["end_time"]))
        event = Event(
            name=data["name"],
            location=data["location"],
            start_time=start,
            end_time=end,
            max_capacity=data["max_capacity"]
        )
        db.session.add(event)
        db.session.commit()
        return jsonify({"message": "Event created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@event_bp.route("/events", methods=["GET"])
def list_events():
    events = Event.query.all()
    return jsonify([{
        "id": e.id,
        "name": e.name,
        "location": e.location,
        "start_time": e.start_time.isoformat(),
        "end_time": e.end_time.isoformat(),
        "max_capacity": e.max_capacity
    } for e in events]), 200
