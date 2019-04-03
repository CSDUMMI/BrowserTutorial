test_mode = "code"


def test_like(local_vars,fun_name,field):
    # call likes 10 times
    # on the first article
    articles = list(local_vars["blog"].keys())
    if articles == []:
        return "Failure: You deleted one of the fields!"
    for i in range(10):
        likes_before = local_vars["blog"][articles[0]][field]
        local_vars[fun_name](articles[0])
        if local_vars["blog"][articles[0]][field] != likes_before+1:
            break
    else:
        return False # No error
    return True # Error

def test(local_vars):
    if not "like" in local_vars or not "dislike" in local_vars:
        return "Failure: like or dislike isn't defined"
    elif test_like(local_vars,"like","likes"):
        return "Failure: your like function doesn't work right"
    elif test_like(local_vars,"dislike","dislikes"):
        return "Failure: your dislike function doesn't work"
    else:
        return "Success"
