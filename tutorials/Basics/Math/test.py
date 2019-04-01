test_mode = "code"

def test(local_vars):
    if not ("area" in local_vars) or not ("rest" in local_vars):
        return "Failure: area or rest aren't defined"
    elif local_vars["area"] != local_vars["site_length"] ** 2:
        return "Failure: area isn't the area of the square"
    elif local_vars["rest"] != local_vars["site_length"] % 2:
        return "Failure: rest isn't the rest of site length and two"
    else:
        return "Success"
