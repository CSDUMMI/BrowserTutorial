import random

test_mode = "code"

def test_gather_xp(gather_xp_fun):
    for i in range(10):
        new_xp = random.randint(1,200)
        player_xp = random.randint(0,150)
        #No max level
        player_level = random.randint(0,10)
        level_threshhold = random.randint(50,150)

        if player_xp >= level_threshhold:
            new_player_level = player_level + 1
            new_player_xp = (player_xp + new_xp) - level_threshhold
            
        else:
        result_dict = {
            "player_level":
        }
        result = result_dict == gather_xp_fun(  new_xp,
                                                player_xp,
                                                player_level,
                                                level_threshhold
                                                )





def test(local_vars):
    gather_xp_fun = local_vars["gather_xp"]
    return test_gather_xp(gather_xp_fun)
