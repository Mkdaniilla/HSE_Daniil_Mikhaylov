def validate_inn(inn: str) -> bool:
    if not inn.isdigit():
        return False

    length = len(inn)

    if length == 10:
        return validate_legal_inn(inn)
    elif length == 12:
        return validate_individual_inn(inn)
    else:
        return False


def validate_legal_inn(inn: str) -> bool:
    weights = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    checksum = sum(int(d) * w for d, w in zip(inn[:9], weights))
    control_digit = checksum % 11
    if control_digit > 9:
        control_digit = control_digit % 10
    return control_digit == int(inn[9])


def validate_individual_inn(inn: str) -> bool:
    weights_1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    weights_2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]

    checksum_1 = sum(int(d) * w for d, w in zip(inn[:10], weights_1))
    control_digit_1 = checksum_1 % 11
    if control_digit_1 > 9:
        control_digit_1 = control_digit_1 % 10

    checksum_2 = sum(int(d) * w for d, w in zip(inn[:11], weights_2))
    control_digit_2 = checksum_2 % 11
    if control_digit_2 > 9:
        control_digit_2 = control_digit_2 % 10

    return control_digit_1 == int(inn[10]) and control_digit_2 == int(inn[11])

if __name__ == "__main__":
    print(validate_inn("7707083893"))    # True (организация)
    print(validate_inn("500100732259"))  # True (физлицо/ИП)
    print(validate_inn("1234567890"))    # False
    print(validate_inn("abcdefghij"))    # False


