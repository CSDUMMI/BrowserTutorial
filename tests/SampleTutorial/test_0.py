"""
Variables in a test script:
test_mode:
    "code": Executes a function and gives it the locals dict that resulted
            of the execution of the resulted code
    "text": Executes a function that gets the code as a string, to regex match
"""
test_mode = "code"

def test(locals_vars):
    # Test if add is defined
    if locals_vars.get('add') == None:
        return "Failure: add function not defined"
    # Test if the add function works
    elif locals_vars['add'](5,5) == 10:
        return "Success" # Success tells the UI that code is good
    else:
        return "Failure: 5 + 5 != 10?????" # If the test didn't work return a error msg
