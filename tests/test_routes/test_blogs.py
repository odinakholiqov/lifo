import json
from tests.utils.blog  import create_random_blog
from schemas.blog import CreateBlog

def test_get_blog(client, db_session):
    blog: CreateBlog = create_random_blog(db=db_session)
    response = client.get(f"blogs/{blog.id}/")
    print(response)
    assert response.status_code == 200
    assert response.json()["title"] == blog.title




# def test_create_blog(client):
#     data = {
#             "title": "test",
#             "context": "test"
#         }
#     response = client.post("/blogs",json=data)
#     assert response.status_code == 201
#     assert response.json()["title"] == "test"
#     assert response.json()["context"] == "test"