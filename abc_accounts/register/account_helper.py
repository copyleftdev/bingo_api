import uuid


def decipher(code, cipher):
    decrypted_code = ""
    o = code
    r = cipher
    i = {}
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]

    for pos, letter in enumerate(r):
        i[letter] = a[pos]

    for letter in o:
        decrypted_code += str(i[letter])
    return decrypted_code


def generate_user_data():
    salt = str(uuid.uuid1())
    email = f"test_{salt}@test.test"
    password = "test123"
    return (email, password)


def get_avatar(gender):
    return "boy_avatar01" if gender == "M" else "girl_avatar01"
