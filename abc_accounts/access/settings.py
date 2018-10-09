from .access import Access
from .path_helper import get_path_id
from .settings_helper import reverse_gender_key


class Settings(Access):
    SETTINGS_ENDPOINT = "/apis/abc/0.1/json/Parent/SetUserSettings/init"

    def __init__(self, account):
        self.domain = account.host
        self.account = account
        super().__init__()

    @property
    def endpoint(self):
        return self.domain + self.SETTINGS_ENDPOINT

    def authenticate(self):
        cookies = self.account.cookies
        self.add_cookies_to_session_from_dict(cookies)

    def send(self, payload):
        payload_string = self.json_encode([[payload]])
        payload = dict(arguments=payload_string)
        r = self.s.post(self.endpoint, payload).json()
        if r.get("success", False) == "TRUE":
            return r.get("payload").get("user_settings")[0]

    def set_grade_level(self, user, level):
        payload = {
            "learning_path_id": get_path_id(level),
            "learning_path_level": level,
            "member_id": int(user.id),
        }
        r = self.send(payload)
        user.level = r.get("learning_path_level", level)

    def swap_gender(self, user):
        next = reverse_gender_key(user.gender)
        payload = {
            "gender": next,
            "member_id": int(user.id),
        }
        r = self.send(payload)
        user.gender = r.get("gender", user.gender)
