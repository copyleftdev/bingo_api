class Admin:
    def __init__(self, name_first, name_last):
        self.id = None
        self.level = None
        self.gender = None
        self.fname = name_first
        self.lname = name_last


class Child:
    def __init__(self, name, level, gender):
        self.id = None
        self.level = level
        self.name = name
        self.gender = gender


class Account:
    def __init__(self, host=None, admin=Admin("Celine", "Dion"), children=[]):
        self.id = None
        self.email = None
        self.password = None
        self.host = None
        self.status = None
        self.cookies = None
        self.active_child = None
        self.admin = admin
        self.children = children
        self.host = host

    def add_child(self, name, level, gender):
        self.active_child = len(self.children)
        self.children.append(Child(name, level, gender))

    @property
    def active_user(self):
        if self.active_child is None:
            return self.admin
        else:
            return self.children[self.active_child]
