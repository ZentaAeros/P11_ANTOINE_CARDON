from server import app
import server

client = app.test_client()

def test_login_and_book_place_on_competition_and_logout():
    # Test login
    email = "john@simplylift.co"
    login = client.post("/showSummary", data={"email": email})

    assert login.status_code == 200

    # Test book open competition
    response = client.get(
        f"/book/{server.competitions[1]['name']}/{server.clubs[0]['name']}"
    )
    assert response.status_code == 200

    # Test deduct points clubs
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


    # Test logout
    logout = client.get('/logout')

    assert logout.status_code == 302