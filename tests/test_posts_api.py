from api.posts_api import PostsAPI


def test_get_all_posts(posts_api):

    response = posts_api.get_all_posts()
    response_body = response.json()

    assert response.status_code == 200
    assert isinstance(response_body, list)
    assert len(response_body) > 0

    first_post = response_body[0]

    assert "userId" in first_post
    assert "id" in first_post
    assert "title" in first_post
    assert "body" in first_post

def test_get_post_by_id(posts_api):

    response = posts_api.get_post_by_id(1)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["id"] == 1
    assert response_body["userId"] == 1
    assert isinstance(response_body["title"], str)
    assert isinstance(response_body["body"], str)
    assert response_body["title"]
    assert response_body["body"]

def test_create_post(posts_api):

    payload = {
        "title": "Electrolux test post",
        "body": "Created through pytest",
        "userId": 1
    }

    response = posts_api.create_post(payload)
    response_body = response.json()

    assert response.status_code == 201
    assert response_body["title"] == payload["title"]
    assert response_body["body"] == payload["body"]
    assert response_body["userId"] == payload["userId"]
    assert "id" in response_body

def test_get_non_existing_post(posts_api):

    response = posts_api.get_post_by_id(9999)

    assert response.status_code == 404
    assert response.json() == {}