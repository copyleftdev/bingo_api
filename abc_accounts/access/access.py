from abc import ABCMeta, abstractmethod
import requests
import json


class Access(metaclass=ABCMeta):
    def __init__(self):
        self.s = requests.Session()

    def __enter__(self):
        self.authenticate()
        return self

    def __exit__(self, *args):
        self.s.__exit__()

    @abstractmethod
    def authenticate(self):
        ...

    def add_cookies_to_session_from_dict(self, cookies):
        jar = requests.cookies.cookiejar_from_dict(cookies)
        self.s.cookies.update(jar)

    def json_encode(self, args):
        return json.dumps(args)
