import argparse
import sys

import account
import register

VALID_DOMAINS = [
    "dev",
    "qtest",
    "test",
]


def is_valid_domain(domain):
    for valid_domain in VALID_DOMAINS:
        if valid_domain in domain:
            return True
    return False


def sanitize_domain(domain):
    d = domain
    # if not is_valid_domain(d):
    #     print("Only qtest, sandboxes, and qdev domains are valid")
    #     sys.exit()
    if not domain:
        print("Please provide a domain [XX].abcmouse.com")
        sys.exit()

    if "http://" in domain:
        print("Only https is valid... redirecitng to https.")
        return d.replace("http://", "https://")
    elif "https" not in domain:
        return "https://" + d
    else:
        return d


if __name__ == "__main__":
    domain = sanitize_domain("cs.qtest.abcmouse.com")
    parent = account.Account(host=domain)
    parent.
    parent.add_child("Denver", 1, "M")
    parent.add_child("Dallas", 7, "F")

    register.new("parent", parent)
    print(f"Done!\tEmail: {parent.email}\tPassword: {parent.password}")
