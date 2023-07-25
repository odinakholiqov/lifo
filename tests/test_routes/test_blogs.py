import json

def test_create_blog(client):
    data = {
            "title": "test",
            "context": "test"
        }
    response = client.post("/blogs",json=data)
    assert response.status_code == 201
    assert response.json()["title"] == "test"
    assert response.json()["context"] == "test"