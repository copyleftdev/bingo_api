def get_path_id(level):
    ids = {
        "0": 7,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 108,
        "6": 104,
        "7": 109,
        "8": 121,
        "9": 136,
        "10": 138,
    }
    return ids.get(str(level), None)
