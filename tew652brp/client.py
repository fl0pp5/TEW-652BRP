import requests

from .core.login import login
from .core.utils import make_routes


class Client:
    def __init__(self, base_url):
        self._base_url = base_url
        self._urls = make_routes(base_url)
        self._session = requests.Session()

    def login(self, username, password):
        return login(self._session, self._urls['login'], username, password)
