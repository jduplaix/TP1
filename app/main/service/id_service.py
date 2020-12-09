import re

def check_id(id_to_check):

    check_status = check_structure(id_to_check) 
    #DEGAGE LES PRINT
    print(check_status)
    if check_status > 0:
        check_status += check_rule_Z(id_to_check)
        #DEGAGE LES PRINT
        print(check_status)
    if check_status == 1:
        check_status += check_key_calculation(id_to_check)
        #DEGAGE LES PRINT
        print(check_status)

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
        #DEGAGE LES PRINT
        print(test_regex.group())
        return 1
    except Exception as e:
        print(e)
        print('<< La structure de l\'identifiant ' + id_to_check + ' ne respecte pas la rêgle ^[A-P|Z][0-9]{9}$')
        return 0


def check_rule_Z(id_to_check):
    id_key = id_to_check[0]
    id_value = int(id_to_check[1:])
    if id_key == "Z" and id_value < 10000000:
        #DEGAGE LES PRINT
        print(id_key)
        print(id_value)
        return 1
    else:
        #DEGAGE LES PRINT
        print(id_key)
        print(id_value)
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
        #DEGAGE LES PRINT
        print(id_value, type(id_value))
        print(key_calc)
    else:
        #DEGAGE LES PRINT
        print(65 + key_calc, " - ", ord(id_key))
        if ord(id_key) == 65 + key_calc:
            return 0
        else:
            return -1
        






