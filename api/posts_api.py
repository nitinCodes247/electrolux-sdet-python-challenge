import requests
from requests import Response

from config.settings import BASE_URL
from utils.logger import get_logger


class PostsAPI:

    logger = get_logger(__name__)

    POSTS_ENDPOINT = "/posts"

    def __init__(self):
        self.session = requests.Session()

    def _get(self, path: str) -> Response:
        return self.session.get(f"{BASE_URL}{path}")


    def _post(self, path: str, payload: dict) -> Response:
        return self.session.post(f"{BASE_URL}{path}",json=payload)

    def get_all_posts(self) -> Response:
        self.logger.info("Fetching all posts")
        return self._get(self.POSTS_ENDPOINT)
    
    def get_post_by_id(self, post_id: int) -> Response:
        self.logger.info(f"Fetching post with id {post_id}")
        return self._get(f"{self.POSTS_ENDPOINT}/{post_id}")


    def create_post(self, payload: dict) -> Response:
        self.logger.info("Creating a new post")
        return self._post(self.POSTS_ENDPOINT, payload)