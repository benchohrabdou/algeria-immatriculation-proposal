import string

ALPHABET = string.ascii_uppercase

def encode_year(year):
    """
    Convertit une année réelle (1985–2084) en code 2 chiffres.
    Exemple :
    1985 -> 85
    2000 -> 00
    2084 -> 84
    """
    if year < 1985 or year > 2084:
        raise ValueError("L'année doit être comprise entre 1985 et 2084.")

    return f"{year % 100:02d}"


def to_base26(num, length=6):
    """Convertit un entier en base 26 (A-Z) avec padding."""
    if num < 0:
        raise ValueError("Le numéro de série doit être positif")

    letters = []
    while num >= 0:
        num, remainder = divmod(num, 26)
        letters.append(ALPHABET[remainder])
        if num == 0:
            break
        num -= 1  # correction

    result = ''.join(reversed(letters))
    return result.rjust(length, 'A')


def generate_plate(vehicle_type, year, serial_number):
    """Génère une immatriculation complète."""
    if not (0 <= vehicle_type <= 9):
        raise ValueError("Le type doit être entre 0 et 9")

    year_code = encode_year(year)
    base26_serial = to_base26(serial_number)

    return f"{vehicle_type}-{year_code}-{base26_serial}"


if __name__ == "__main__":
    print(generate_plate(0, 2024, 152347))  # exemple
    print(generate_plate(2, 2019, 42))
