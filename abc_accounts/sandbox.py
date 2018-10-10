from account import Account
import register
import unittest
import json
import requests
import time

TARGET_URL = "https://www.abcmouse.com"


def account_create():
    domain = TARGET_URL
    parent = Account(domain)
    parent.add_child("Student 1", 2, "M")
    parent.add_child("Student 2", 7, "F")
    register.new('parent',parent)
    return [parent.email, parent.password]

def account_record(uname, password):
    login_endpoint = "/apis/mws/0.3/json/Member/Login/init"
    auth = [uname, password]
    args = dict(arguments=json.dumps(auth))
    req = requests.post(TARGET_URL + login_endpoint, data=args)
    res = req.json()
    return res



account = account_create()
uname = account[0]
password = account[1]
print(uname, password)
master_record = account_record(uname, password)

print(master_record)


class OnboardingAPITest(unittest.TestCase):

    def test_end_end_account_creation_paytech(self):
        account_login_action = master_record['success']
        self.assertEqual(account_login_action, "TRUE")

    def test_master_account_id_is_of_type_integer(self):
        account_id = master_record['payload', 'master_account_member_id']
        self.assertTrue(type(account_id), int)

    def test_master_account_type_group_is_set_to_parent(self):
        mast_account_type = master_record['payload']['master_account_account_type_group']
        self.assertEqual(mast_account_type, "parent")


if __name__ == '__main__':
    unittest.main()
