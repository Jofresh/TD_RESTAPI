def egg_parser(egg) -> dict:
    return {
        "origin": egg["origin"],
        "color": egg["color"],
        "registration": egg["registration"],
    }


def extract_weight(registration: str):
    return registration[:2]


def extract_country(registration: str):
    return registration[3:5]


def extract_day(registration: str):
    return registration[8:10]


def extract_month(registration: str):
    return registration[10:12]
