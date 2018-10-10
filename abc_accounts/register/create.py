import requests


def create(Generator):
    with requests.Session() as s:
        Generator.set_env(s)
        Generator.subscribe()
        Generator.onboard()
        Generator.complete()
        return Generator.account


class AccountCreator:
    def __init__(self, account):
        self.account = account
        self.host = account.host
        self.session = None

    def set_env(self, session, timeout=6):
        self.session = session
        self.timeout = timeout

    def get(self, path):
        return self.session.get(self.host+path, timeout=self.timeout)

    def post(self, path, data):
        return self.session.post(self.host+path,
                                 data=data,
                                 timeout=self.timeout)

    def get_session_cookies(self):
        return self.session.cookies.get_dict()

    def subscribe():
        raise NotImplementedError

    def onboard():
        raise NotImplementedError

    def complete():
        raise NotImplementedError
