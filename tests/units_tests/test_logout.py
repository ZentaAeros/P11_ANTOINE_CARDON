from server import app

client = app.test_client()

def test_logout():
    response = client.get('/logout')

    assert response.status_code == 302