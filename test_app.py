from app import app


def test_home():
    client = app.test_client()
    assert client.get("/").status_code == 200


def test_add():
    client = app.test_client()
    assert client.get("/add?a=2&b=3").get_json()["result"] == 6
