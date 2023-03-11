from server import app
import server

client = app.test_client()

def test_deduct_points_after_booking_competition():
    server.clubs[0]["points"] = 10
    clubs_points_before_booking = server.clubs[0]["points"]

    booking = client.post(
        "/purchasePlaces",
        data={
            "places": 5,
            "club": server.clubs[0]["name"],
            "competition": server.competitions[0]["name"],
        },
    )

    clubs_points_after_booking = server.clubs[0]["points"]

    expected_value = 5

    assert clubs_points_before_booking == 10
    assert "Great-booking complete!" in booking.data.decode()
    assert clubs_points_after_booking == expected_value
