test_mode = "code"

def test(local_vars):
    if not "head" in local_vars or not "tail" in local_vars:
        return "Failure: head or tail isn't defined"
    elif local_vars["head"] != local_vars["splitMe"][0]:
        return "Failure: head isn't the head of splitMe"
    elif local_vars["tail"] != local_vars["splitMe"][0:]:
        return "Failure: tail isn't the tail of splitMe"
    else:
        return "Success"
