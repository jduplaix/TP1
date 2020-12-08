import re

response = {
            "status":"not_checked",
            "request":"none",
            "result":2
        }

def check_id(id_to_check):

    check_structure(id_to_check) 


    return response


def check_structure(id_to_check):
    global response
    if response['result'] > 0:
        response['request'] = id_to_check
        regex = re.compile('^[A-P|Z][0-9]{9}$')
        test_regex = regex.match(id_to_check)
        ## Si l'ID ne match pas la REGEX, il sera un objet de type NoneType
        ## sur lequel on ne peut pas .group()
        try:
            isinstance(test_regex.group(), str)
            response['status'] = "success"
            response['result'] = 1
        except Exception as e:
            print('Structure de l\'identifiant ' + id_to_check + ' invalide:')
            print(e)
            response['status'] = "failed"
            response['result'] = 0

#def check_rule_2(id_to_check):





