import os

from .access import Access
from .path_helper import get_path_id


_user = os.environ["ADMIN_USER"]
_pwd = os.environ["ADMIN_PASS"]
_target = os.environ["DATABASE_IP"]
_host = os.environ["TARGET"]


class Admin(Access):
    DOMAIN = "https://admin.aofl.com"
    LEGACY_ENDPOINT = DOMAIN + "/eventhandler.php"

    @property
    def database_env(self):
        return _host.replace("https://", "")

    def authenticate(self):
        credentials = {
            "user": _user,
            "pass": _pwd
        }
        self.s.post(self.DOMAIN, credentials)

    def legacy_send(self, payload):
        self.s.post(self.LEGACY_ENDPOINT, payload)

    def send(self, endpoint, payload):
        args = self.json_encode(payload)
        payload = dict(
            arguments=args,
            database_environment=self.database_env
        )
        self.s.post(self.DOMAIN+endpoint, payload)

    def convert_to_test_account(self, account):
        user_id = account.id
        payload = {
            "action": "inline",
            "event": "userlookup",
            "objectid": "account_type",
            "server": _target,
            "userid": user_id,
            "value": 6,
        }
        self.legacy_send(payload)

    def complete_activities_on_lp(self, user, count):
        e = "/apis/cms/0.1/json/User/SetBiomeProgress/init"
        payload = [user.id, get_path_id(user.level), count]
        self.send(e, payload)
