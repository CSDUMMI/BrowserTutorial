test_mode = "code"

def test(local_vars):
    if not ("commits_a_crime" in local_vars):
        return "Failure: commits_a_crime isn't defined"
    elif local_vars["commits_a_crime"] != (local_vars["drives_a_car"] and not local_vars["has_a_license"]):
        return "Failure: commits_a_crime isn't defined right"
    else:
        return "Success"
