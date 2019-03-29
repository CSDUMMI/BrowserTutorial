import random, json

test_mode = "code"

def test(local_vars):
    if not "is_even" in local_vars:
        return "Failure: is_even isn't defined"
    elif local_vars["is_even"] != (local_vars["num"] % 2 == 0):
        return "Failure: is_even is wrong"
    else:
        return "Success"
