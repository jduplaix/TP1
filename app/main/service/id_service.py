import re

check_status = 0

def check_id(id_to_check):

    check_structure(id_to_check)
    if check_status == 0:
        response = {
            "status":"success",
            "request":id_to_check,
            "result":1
        }
    else:
        response = {
            "status":"failed",
            "request":id_to_check,
            "result":0
        }
    return response


def check_structure(id_to_check):
    regex = re.compile('^[A-P|Z][0-9]{9}$')
    test_regex = regex.match(id_to_check)
    ## Si l'ID ne match pas la REGEX, il sera un objet de type NoneType
    ##  sur lequel on ne peut pas .group()
    try:
        isinstance(test_regex.group(), str) 
    except Exception as e:
        print('Structure de l\'identifiant ' + id_to_check + ' invalide:')
        print(e)
        global check_status
        check_status += 1



