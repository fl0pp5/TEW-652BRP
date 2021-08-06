import requests

from tew652brp.core.login import login
from tew652brp.core.utils import make_routes
from tew652brp.core.access.virtual import get_virtual_server_list


class Client:
    def __init__(self, base_url):
        self._base_url = base_url
        self._urls = make_routes(base_url)
        self._session = requests.Session()

    def login(self, username, password):
        return login(self._session, self._urls['login'], username, password)

    def get_virtual_server_list(self):
        return get_virtual_server_list(self._session, self._urls['get_set'])
