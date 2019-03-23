"""
Variables in a test script:
test_mode:
    "code": Executes a function and gives it the locals dict that resulted
            of the execution of the resulted code
    "text": Executes a function that gets the code as a string, to regex match
"""
test_mode = "code"

def test(local_vars):
    # Test if add is defined
    if local_vars.get("add") == None:
        return "Failure: No add function defined"
    elif locals_vars["add"](5,5) == 10:
        return "Success"
    else:
        return "Failure: 5 + 5 != 10 ????"
