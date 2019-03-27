test_mode = "code"

def test(local_vars):
    if not "char_4" in local_vars or not "char_2" in local_vars:
        return "Failure: char_4 or char_2 aren't defined"
    elif local_vars["char_2"] != '2':
        return "Failure: char_2 isn't the second character"
    elif local_vars["char_4"] != '4':
        return "Failure: char_4 isn't the fourth character"
    else:
        return "Success"
