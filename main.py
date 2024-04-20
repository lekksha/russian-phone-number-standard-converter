def filter_odd_symbols(i):
    symbols = "-()+"
    if i in symbols:
        return False
    else:
        return True


def phone_to_default(phone_number, region_code="495"):  # Moscow code as default for short phone numbers
    filtered_phone_number = ''.join(filter(filter_odd_symbols, phone_number))
    if len(filtered_phone_number) > 10:
        filtered_phone_number = filtered_phone_number[len(filtered_phone_number) - 10:len(filtered_phone_number)]
    elif len(filtered_phone_number) == 7:
        filtered_phone_number = region_code + filtered_phone_number
    return filtered_phone_number
