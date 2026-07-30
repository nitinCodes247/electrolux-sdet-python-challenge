import requests
from requests import Response

from config.settings import BASE_URL


class PostsAPI:

    POSTS_ENDPOINT = "/posts"

    def __init__(self):
        self.session = requests.Session()

    def _get(self, path: str) -> Response:
        return self.session.get(f"{BASE_URL}{path}")


    def _post(self, path: str, payload: dict) -> Response:
        return self.session.post(f"{BASE_URL}{path}",json=payload)

    def get_all_posts(self) -> Response:
        return self._get(self.POSTS_ENDPOINT)


    def get_post_by_id(self, post_id: int) -> Response:
        return self._get(f"{self.POSTS_ENDPOINT}/{post_id}")


    def create_post(self, payload: dict) -> Response:
        return self._post(self.POSTS_ENDPOINT, payload)