import re


def create_id(value):
    try:
        if isinstance(value, str) and len(value) == 9:
            if int(value) < 10000000:
                id = "Z" + value
            else:
                id = attach_id_key(value)
            response = {
                "status": "success",
                "request": value,
                "result": id
            }
            return response
        else:
            return 'bad_value'
    except Exception as e:
        print(e)
        return 'bad_value'


def attach_id_key(value):
    key_calc = 16
    value_calc = value
    while key_calc > 15:
        key_calc = 0
        for car in value_calc:
            key_calc += int(car)
        value_calc = str(key_calc)
    return chr(65 + key_calc) + value


def check_id(id_to_check):
    check_status = check_structure(id_to_check) 
    if check_status > 0:
        check_status += check_rule_Z(id_to_check)
    if check_status == 1:
        check_status += check_key_calculation(id_to_check)

    response = {
        "status": "success" if check_status > 0 else "failed",
        "request": id_to_check,
        "result": check_status if check_status == 0 else 1
    }
    return response


def check_structure(id_to_check):

    regex = re.compile('^[A-P|Z][0-9]{9}$')
    test_regex = regex.match(id_to_check)
    ## Si l'ID ne match pas la REGEX, test_regex = null
    try:
        isinstance(test_regex.group(), str)
        return 1
    except Exception as e:
        print(e)
        print('<< La structure de l\'identifiant ' + id_to_check + ' ne respecte pas la rêgle ^[A-P|Z][0-9]{9}$')
        return 0


def check_rule_Z(id_to_check):
    id_key = id_to_check[0]
    id_value = int(id_to_check[1:])
    if id_key == "Z" and id_value < 10000000:
        return 1
    else:
        return 0

def check_key_calculation(id_to_check):
    id_key = id_to_check[0]
    id_value = id_to_check[1:]
    key_calc = 16
    while key_calc > 15:
        key_calc = 0
        for car in id_value:
            key_calc += int(car)
        id_value = str(key_calc)
    else:
        if ord(id_key) == 65 + key_calc:
            return 0
        else:
            return -1
        






