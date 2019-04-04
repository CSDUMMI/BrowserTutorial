import random

test_mode = "code"


def test_analyse(analyse):
    # Test what happens if both votes are equal:
    if analyse(50,50) != "against":
        return "Failure: analyse doesn't return \"against\" by analyse(50,50)"
    else:
        # Test 10 random cases
        for i in range(10):
            votes_for = random.randint(1,100)
            votes_against = random.randint(1,100)
            result = analyse(votes_for,votes_against)
            if votes_against >=  votes_for:
                should_be_result = "against"
            else:
                should_be_result = "for"

            if result != should_be_result:
                return """
                    Failure: analyse should return: \"{}\"<br>
                    But it returned \"{}\"<br>
                    votes_for = {}<br>votes_against = {}
                    """.format(should_be_result,result,votes_for,votes_against)
        else:
            return "Success"

def test(local_vars):

    if not "analyse" in local_vars:
        return "Failure: analyse isn't defined"
    else:
        return test_analyse(local_vars["analyse"])
