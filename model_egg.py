from pydantic import BaseModel, validator

COUNTRIES_CODE = ["FR", "BE", "AL", "LU", "SU", "IT", "ES"]

MONTHS_IN_NUMBER = {
    "JA": "01",
    "FE": "02",
    "MA": "03",
    "AV": "04",
    "MI": "05",
    "JU": "06",
    "JL": "07",
    "AO": "08",
    "SE": "09",
    "OC": "10",
    "NO": "11",
    "DE": "12",
}

COLORS = ["grey", "brown", "white"]


class ModelEgg(BaseModel):
    origin: str
    color: str
    registration: str

    @validator("color")
    def is_color_valid(cls, v):
        if v not in COLORS:
            raise ValueError(f"Egg color must be: {COLORS}")
        return v

    @validator("registration")
    def is_valid(cls, v):
        if len(v) != 12:
            raise ValueError("Egg registration must have a length of 12.")

        weight = v[:2]
        if not weight.isdigit():
            raise ValueError("The egg registration weight must be 2 numbers.")
        if int(weight) % 5 != 0:
            raise ValueError("The egg weight must be a multiple of 5.")

        dash = v[2]
        if dash != "-":
            raise ValueError(
                "The third character of the egg registration must be a dash/hyphen."
            )

        country = v[3:5]
        if country not in COUNTRIES_CODE:
            raise ValueError(f"Egg registration country code must be: {COUNTRIES_CODE}")

        origin_code = v[5:8]
        if not origin_code.isdigit():
            raise ValueError("Egg registration origin must be 3 numbers.")
        if origin_code[0] == origin_code[2]:
            raise ValueError("Egg registration cannot be a palindrome.")

        day = v[8:10]
        if not day.isdigit():
            raise ValueError("Egg registration day must be 2 numbers.")
        if int(day) not in range(1, 31 + 1):
            raise ValueError("Egg registration day must be between 01 and 31 included.")

        month = v[10:12]
        if month not in MONTHS_IN_NUMBER.keys():
            raise ValueError(
                f"Egg registration month must be: {MONTHS_IN_NUMBER.keys()}"
            )

        if day == MONTHS_IN_NUMBER[month]:
            raise ValueError(
                "Egg registration day and month cannot be the same (01JA is not possible)"
            )

        return v
