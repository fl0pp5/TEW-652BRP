import requests

from tew652brp.core.login.handler import LoginHandler
from tew652brp.core.access.virtual.handler import VirtualHandler


class Client:
    def __init__(self, base_url):
        self._base_url = base_url
        self._session = requests.Session()

        self.virtual = VirtualHandler(self._session, self._base_url)
        self.login = LoginHandler(self._session, self._base_url)
