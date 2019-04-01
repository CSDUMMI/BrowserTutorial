test_mode = "code"

def test(local_vars):
    if not "is_not_allowed_to_drive" in local_vars:
        return "Failure: is_not_allowed_to_drive isn't defined"
    elif local_vars["is_not_allowed_to_drive"] != local_vars["has_a_license"] and local_vars["drives_a_car"]:
        return "Failure: is_not_allowed_to_drive is wrong."
    else:
        return "Success"
