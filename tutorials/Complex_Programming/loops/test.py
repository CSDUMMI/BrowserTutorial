
test_mode = "code"


def test(local_vars):
        balance = local_vars['balance']

        for i in local_vars['debts']:
            balance -= i

        if local_vars['balance'] == balance
