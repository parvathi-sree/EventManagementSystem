def test_register_attendee(client):
    # First create an event
    client.post("/events", json={
        "name": "PySummit",
        "location": "Mumbai",
        "start_time": "2025-08-10T09:00:00",
        "end_time": "2025-08-10T18:00:00",
        "max_capacity": 1
    })
    event_id = 1

    # Register an attendee
    response = client.post(f"/events/{event_id}/register", json={
        "name": "Alice",
        "email": "alice@example.com"
    })
    assert response.status_code == 200
    assert response.get_json()["message"] == "Registration successful"


def test_prevent_duplicate_registration(client):
    event_id = 1
    client.post("/events", json={
        "name": "RepeatCheck",
        "location": "Online",
        "start_time": "2025-08-12T10:00:00",
        "end_time": "2025-08-12T12:00:00",
        "max_capacity": 2
    })

    data = {"name": "Bob", "email": "bob@example.com"}
    client.post(f"/events/{event_id}/register", json=data)
    response = client.post(f"/events/{event_id}/register", json=data)
    assert response.status_code == 400
    assert "Already registered" in response.get_json()["error"]


def test_prevent_overbooking(client):
    event_id = 1
    client.post("/events", json={
        "name": "LimitEvent",
        "location": "Zoom",
        "start_time": "2025-09-01T09:00:00",
        "end_time": "2025-09-01T11:00:00",
        "max_capacity": 1
    })

    client.post(f"/events/{event_id}/register", json={
        "name": "Carol",
        "email": "carol@example.com"
    })

    response = client.post(f"/events/{event_id}/register", json={
        "name": "Dave",
        "email": "dave@example.com"
    })
    assert response.status_code == 400
    assert "Event full" in response.get_json()["error"]
