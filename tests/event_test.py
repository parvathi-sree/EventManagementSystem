

def test_create_event(client):
    response = client.post("/events", json={
        "name": "FlaskConf",
        "location": "Delhi",
        "start_time": "2025-06-20T10:00:00",
        "end_time": "2025-06-20T17:00:00",
        "max_capacity": 100
    })
    assert response.status_code == 201
    assert response.get_json()["message"] == "Event created"


def test_get_events(client):
    client.post("/events", json={
        "name": "MiniCon",
        "location": "Chennai",
        "start_time": "2025-07-01T09:00:00",
        "end_time": "2025-07-01T16:00:00",
        "max_capacity": 50
    })
    response = client.get("/events")
    assert response.status_code == 200
    events = response.get_json()
    assert len(events) == 1
    assert events[0]["name"] == "MiniCon"
