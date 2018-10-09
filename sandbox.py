from abc_accounts.account import Account
import abc_accounts.register


domain = "cs.abcmouse.com"
parent = Account(host=domain)
parent.add_child("Student 1", 2, "M")
parent.add_child("Student 2" ,7, "F")
register.new('parent', parent)
print(parent.email, parent.password)