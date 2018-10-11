import json
import register.parent_helper as parent
from .create import AccountCreator
from .account_helper import decipher, generate_user_data, get_avatar


class SubscriptionEndpoints:
    LANDING = "/ws/msl/0.1/json/AuthorizationCode/Generate/init"
    PROSPECT = "/ws/msl/0.1/json/Prospect/Subscribe/init"
    SAVE_PARENT = "/apis/abc/0.1/json/Onboarding/SaveParent/init"
    CREATE_CHILD = "/apis/abc/0.1/json/Onboarding/AddChild/init"
    SAVE_CHILD = "/apis/abc/0.1/json/Onboarding/SaveChild/init"
    SET_AVATAR = "/apis/abc/0.1/json/Onboarding/SetPremadeAvatar/init"
    SAVE_PET = "/apis/abc/0.1/json/Onboarding/QueueSavePet/init"
    CONFIRM = "/apis/abc/0.1/json/Onboarding/Confirm/init"
    ACTIVATE = "/regpath/regdone"


ENDPOINT = SubscriptionEndpoints()


class Parent(AccountCreator):
    def send(self, endpoint, args=[]):
        args = dict(arguments=json.dumps(args))
        res = self.post(endpoint, args).json()

        if res.get("success"):
            return res.get("payload")

    def fetch(self, endpoint):
        res = self.get(endpoint).json()

        if res.get("success"):
            return res.get("payload")

    def subscribe(self):
        email, password = generate_user_data()
        init_subscription = self.get(ENDPOINT.LANDING).json()
        payload = init_subscription.get("payload", False)

        if payload:
            form_id = payload.get("id")
            auth_code = payload.get("auth_code")
            cipher = payload.get("cipher")
            if auth_code and cipher:
                authorization_code = decipher(auth_code, cipher)
        args = parent.subscription_prospect(email,
                                            password,
                                            form_id,
                                            authorization_code)
        res = self.send(ENDPOINT.PROSPECT, args)
        self.account.email = email
        self.account.password = password
        self.account.id = res.get("member_id")

    def onboard(self):
        parent_info = [{
            "first_name": self.account.admin.fname,
            "last_name": self.account.admin.lname,
        }]
        self.send(ENDPOINT.SAVE_PARENT, parent_info)

        for child in self.account.children:
            child.id = self.add_child(child.name, child.gender, child.level)

    def add_child(self, name, gender, level):
        init_child = self.send(ENDPOINT.CREATE_CHILD)
        child_id = init_child.get("member_id")
        child_info = [child_id, {
            "first_name": name,
            "gender": gender,
            "level": level,
            "teacher": 5,
            "child_relation": 11,

        }]
        self.send(ENDPOINT.SAVE_CHILD, child_info)
        self.send(ENDPOINT.SET_AVATAR, [child_id, get_avatar(gender)])
        self.send(ENDPOINT.SAVE_PET, [child_id, 105400, 153000])
        return child_id

    def complete(self):
        self.send(ENDPOINT.CONFIRM)
        self.get(ENDPOINT.ACTIVATE)
        self.account.cookies = self.get_session_cookies()
