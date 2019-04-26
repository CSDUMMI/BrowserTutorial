import json

test_mode = "code"


def test(local_vars):
        balance =   json.load(
                    open("tutorials/Complex_Programming/loops/vars.json")
                    )['balance']
    

        for i in local_vars['debts']:
            balance -= i

        if not (local_vars['balance'] == balance):
            return "Failure: balance is wrong"
        else:
            return "Success"
