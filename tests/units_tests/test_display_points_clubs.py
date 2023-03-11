from server import app

client = app.test_client()

def test_display_points_clubs():
    response = client.get('/displayPoints')

    assert response.status_code == 200
    assert "Points / clubs" in response.data.decode()