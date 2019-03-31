test_mode = "code"

def test(local_vars):
    if "has_enough_xp" in local_vars:
        has_enough_xp = local_vars['xp'] * 10 >= local_vars["level_num"]
        if local_vars["has_enough_xp"] == has_enough_xp
