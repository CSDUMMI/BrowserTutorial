test_mode = "code"

def test(local_vars):
    if not "x" in local_vars or not "zwei_hoch_acht" in local_vars:
        return "Failure: x or zwei_hoch_acht isn't defined"
    elif local_vars.get("x") != 50 % 8:
        return "Failure: x isn't 50 modulo 8"
    elif local_vars.get("zwei_hoch_acht") != 2 ** 8:
        return "Failure zwei_hoch_acht isn't 2 to the 8th power"
    else:
        return "Success"
