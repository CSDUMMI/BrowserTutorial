import random
test_mode = "code"

def rand_vars():
    vars = json.load(open("tutorials/Complex_Programming/comparisons/vars.json"))
    vars["xp"] = random.randint(0,100)
    vars["level_threshhold"] = random.randint(25,75)
    json.dump(open("tutorials/Complex_Programming/comparisons/vars.json"),vars)

def test(local_vars):
    vars = json.load(open("tutorials/Complex_Programming/comparisons/vars.json"))
    old_xp = vars["xp"]
    old_level = vars["level"]
    level_threshhold = vars["level_threshhold"]
    enough_xp = old_xp > level_threshhold

    if enough_xp:
        xp_is_reseted = local_vars["xp"] == 0
        level_upgraded = local_vars["level"] == old_level +1

        if not xp_is_reseted:
            ret_msg ="Failure: xp wasn't reseted to zero"
        elif not level_upgraded:
            ret_msg ="Failure: level isn't upgraded"
        else:
            ret_msg ="Success"
    else:
        xp_modified = local_vars["xp"] != old_xp
        level_modified = local_vars["level"] != old_level

        if xp_modified:
            ret_msg ="Failure: You change xp, though you shouldn't"
        elif level_modified:
            ret_msg = "Failure: You changed level, though you shouldn't"

    rand_vars()
    return ret_msg
