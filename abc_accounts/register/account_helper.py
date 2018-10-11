import uuid
import random

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
    boy_avatars = ['boy_avatar01', 'boy_avatar02', 'boy_avatar03', 'boy_avatar04', 'boy_avatar05', 'boy_avatar06',
               'boy_avatar07', 'boy_avatar08', 'boy_avatar09', 'boy_avatar10', 'boy_avatar11', 'boy_avatar12',
               'boy_avatar13', 'boy_avatar14', 'boy_avatar15', 'boy_avatar16']
    girl_avatars = ['girl_avatar01', 'girl_avatar02', 'girl_avatar03', 'girl_avatar04', 'girl_avatar05', 'girl_avatar06',
                'girl_avatar07', 'girl_avatar08', 'girl_avatar09', 'girl_avatar10']

    return random.choice(boy_avatars) if gender == "M" else random.choice(girl_avatars)
