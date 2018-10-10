from account import Account
import register
import unittest
import json
import requests
import time


class OnboardingAPITest(unittest.TestCase):

    def setUp(self):
        self.login_endpoint = "/apis/mws/0.3/json/Member/Login/init"
        self.billing_endpoint = "/apis/mws/0.3/json/Parent/GetBillingInfo/init"
        self.domain = "https://cs.qtest.abcmouse.com"
        self.parent = Account(host=self.domain)
        self.parent.add_child("Student 1", 2, "M")
        self.parent.add_child("Student 2", 7, "F")
        time.sleep(10)
        register.new('parent', self.parent)
        self.user_name = self.parent.email
        self.password = self.parent.password


    def test_end_end_account_creation_paytech(self):
        creds = [self.user_name, self.password]
        args = dict(arguments=json.dumps(creds))
        req = requests.post(self.domain + self.login_endpoint, data=args)
        res = req.json()
        account_login_action = res['success']
        self.assertEqual(account_login_action, "TRUE")

    def test_master_account_id_is_of_type_integer(self):
        creds = [self.user_name, self.password]
        args = dict(arguments=json.dumps(creds))
        req = requests.post(self.domain + self.login_endpoint, data=args)
        res = req.json()
        account_id = res['payload', 'master_account_member_id']
        self.assertTrue(type(account_id), type(int))

    def test_master_account_type_group_is_set_to_parent(self):
        creds = [self.user_name, self.password]
        args = dict(arguments=json.dumps(creds))
        req = requests.post(self.domain + self.login_endpoint, data=args)
        res = req.json()
        mast_account_type = res['payload']['master_account_account_type_group']
        self.assertEqual(mast_account_type, "parent")


if __name__ == '__main__':
    unittest.main()
