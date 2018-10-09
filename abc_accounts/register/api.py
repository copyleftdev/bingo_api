from .create import create
from .Parent import Parent


def new(account_type, account):
    supported_accounts = dict(
        parent=Parent,
    )
    builder = supported_accounts.get(account_type.lower())
    return create(builder(account))
