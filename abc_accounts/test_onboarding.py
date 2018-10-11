from account import Account, Admin
import register
import unittest
import json
import requests
import time
import random
from faker import Faker

# Faker used to Radomly generate  artifact  like names, numbers
fake = Faker()

TARGET_URL = "https://dl.qtest.abcmouse.com"

parent_f_name = fake.first_name()
parent_l_name = fake.last_name()

sex_opt = ["M", "F"]
child_1 = {"name": fake.first_name(), "grade": random.randint(1, 7),
           "sex": random.choice(sex_opt)}
child_2 = {"name": fake.first_name(), "grade": random.randint(1, 7),
           "sex": random.choice(sex_opt)}
child_3 = {"name": fake.first_name(), "grade": random.randint(1, 7),
           "sex": random.choice(sex_opt)}



def account_create():
    domain = TARGET_URL
    parent = Account(host=domain, admin=Admin(parent_f_name, parent_l_name))

    for x in (child_1, child_2, child_3):
        parent.add_child(x['name'], x['grade'], x['sex'])
    register.new('parent', parent)
    return [parent.email, parent.password]


def account_record(uname, password):
    login_endpoint = "/apis/mws/0.3/json/Member/Login/init"
    auth = [uname, password]
    args = dict(arguments=json.dumps(auth))
    req = requests.post(TARGET_URL + login_endpoint, data=args)
    res = req.json()
    return res


def get_family_details(token):
    family_endpoint = "/apis/mws/0.3/json/User/GetFamilyInfo/init"
    payload = {"token": token}
    req = requests.post(TARGET_URL + family_endpoint, data=payload)
    res = req.json()
    return res

def get_subscription_info(token):
    sub_endpoint = "/apis/mws/0.3/json/Parent/GetSubscriptionInfo/init"
    payload = {"token": token}
    req = requests.post(TARGET_URL + sub_endpoint, data=payload)
    res = req.json()
    return res


account = account_create()

uname = account[0]
password = account[1]
print(uname, password)
master_record = account_record(uname, password)

session_token = master_record['payload']['token']
family_record = get_family_details(session_token)
sub_info = get_subscription_info(session_token)

# print(master_record)
# print(family_record)


class OnboardingAPITest(unittest.TestCase):

    @unittest.skip("off")
    def test_end_end_account_creation_paytech(self):
        account_login_action = master_record['success']
        self.assertEqual(account_login_action, "TRUE")

    @unittest.skip("off")
    def test_master_account_id_is_of_type_integer(self):
        account_id = master_record['payload']['master_account_member_id']
        self.assertTrue(type(account_id), int)

    @unittest.skip("off")
    def test_master_account_type_group_is_set_to_parent(self):
        mast_account_type = master_record['payload']['master_account_account_type_group']
        self.assertEqual(mast_account_type, "parent")

    @unittest.skip("off")
    def test_rotation_assignment_returns_entries(self):
        rotations = master_record['payload']['rotations']
        self.assertTrue(len(rotations) > 0)

    @unittest.skip("off")
    def test_rotation_analytics_flags_are_set_to_true(self):
        analytics_flags = []
        all_true = []
        rotations = master_record['payload']['rotations']
        for x in range(len(rotations)):
            all_true.append(True)

        for k, v in rotations.items():
            analytics_flags.append(v['send_analytics'])

        self.assertEqual(analytics_flags, all_true)

    @unittest.skip("off")
    def test_all_rotation_status_is_set_to_active(self):
        status_flags = []
        all_active = []
        rotations = master_record['payload']['rotations']
        for x in range(len(rotations)):
            all_active.append("ACTIVE")

        for k, v in rotations.items():
            status_flags.append(v['status'])

        self.assertEqual(status_flags, all_active)

    @unittest.skip("off")
    def test_parent_name_is_set_correctly(self):
        members = family_record['payload']['member_info']
        for member in members:
            if 'parent' in member['type_of_user']:
                assertion_name = member['firstname']
        self.assertEqual(assertion_name, parent_f_name)

    @unittest.skip("off")
    def test_childs_names_are_set_correctly(self):
        members = family_record['payload']['member_info']
        assertion_names = []
        names = [child_1['name'], child_2['name'], child_3['name']]

        for member in members:
            if 'child' in member['type_of_user']:
                assertion_names.append(member['firstname'])
        self.assertListEqual(names, assertion_names)

    def test_current_payments_type_is_credit_card(self):
        payment_info = sub_info['payload']['subscription_info']
        self.assertEqual('credit card', payment_info['current_payment_type'])

    def test_subscription_is_set_to_monthly(self):
        payment_info = sub_info['payload']['subscription_info']
        monthly = payment_info['subscription']
        self.assertEqual(monthly, "Monthly")







if __name__ == '__main__':
    unittest.main()
