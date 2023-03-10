from server import app
import server

client = app.test_client()

server.competitions = [
    {"name": "closedCompetition", "date": "2020-03-05 23:14:00", "numberOfPlaces": "6"},
    {"name": "openCompetition", "date": "2024-03-05 23:14:00", "numberOfPlaces": "6"},
]

server.clubs = [
    {"name": "name of the club", "email": "john@simplylift.co", "points": "8"}
]


def test_booking_with_more_points_than_available():
    server.clubs[0]["points"] = "4"

    response = client.post(
        "/purchasePlaces",
        data={
            "places": 5,
            "club": server.clubs[0]["name"],
            "competition": server.competitions[0]["name"],
        },
    )

    assert "Solde de points insuffisant" in response.data.decode()