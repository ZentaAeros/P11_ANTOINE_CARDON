from server import app

client = app.test_client()


def test_login_with_bad_mail():
    email = "thismaildoesnotexist@gudlft.co"
    response = client.post("/showSummary", data={"email": email})

    assert response.status_code == 401
    assert "Compte inexistant" in response.data.decode()
