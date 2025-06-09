from flask import Blueprint, request, jsonify
from models import Event, Attendee
from app import db

registration_bp = Blueprint('registration', __name__)


@registration_bp.route("/events/<int:event_id>/register", methods=["POST"])
def register_attendee(event_id):
    data = request.get_json()
    event = Event.query.get_or_404(event_id)
    if Attendee.query.filter_by(event_id=event_id, email=data["email"]).first():
        return jsonify({"error": "Already registered"}), 400
    if len(event.attendees) >= event.max_capacity:
        return jsonify({"error": "Event full"}), 400

    attendee = Attendee(name=data["name"], email=data["email"], event_id=event_id)
    db.session.add(attendee)
    db.session.commit()
    return jsonify({"message": "Registration successful"}), 200


@registration_bp.route('/events/<int:event_id>/attendees', methods=['GET'])
def get_attendees(event_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 2, type=int)

    event = Event.query.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    attendees_query = Attendee.query.filter_by(event_id=event_id)
    total = attendees_query.count()
    attendees = attendees_query.offset((page - 1) * per_page).limit(per_page).all()

    data = [
        {
            "id": attendee.id,
            "name": attendee.name,
            "email": attendee.email,
            "registered_at": attendee.created_at.isoformat()
        }
        for attendee in attendees
    ]

    return jsonify({
        "total": total,
        "page": page,
        "per_page": per_page,
        "pages": (total + per_page - 1) // per_page,  # ceil-style
        "attendees": data
    })