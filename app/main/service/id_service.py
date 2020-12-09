import re

def check_id(id_to_check):

    check_status = check_structure(id_to_check) 
    if check_status > 0:
        check_status = check_rule_Z(id_to_check)
    if check_status == 0:
        check_status = check_calculation(id_to_check)


    response = {
        "status": "success" if check_status > 0 else "failed",
        "request": id_to_check,
        "result": check_status
    }
    return response

def check_structure(id_to_check):

    regex = re.compile('^[A-P|Z][0-9]{9}$')
    test_regex = regex.match(id_to_check)
    ## Si l'ID ne match pas la REGEX, test_regex = null
    try:
        isinstance(test_regex.group(), str)
        print(test_regex.group())
        return 1
    except Exception as e:
        print('Structure de l\'identifiant ' + id_to_check + ' invalide:')
        print(e)
        return 0


def check_rule_Z(id_to_check):
    id_key = id_to_check[0]
    id_value = int(id_to_check[1:])
    if id_key == "Z" and id_value < 10000000:
        print(id_key)
        print(id_value)
        return 1
    else:
        print(id_key)
        print(id_value)
        return 0

def check_calculation(id_to_check):
    print('calc')
    return 1






