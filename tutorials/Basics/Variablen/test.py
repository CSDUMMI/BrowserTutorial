test_mode = "code"

def test(local_vars):
    if not (local_vars.get("eine_dezimal_Zahl") or local_vars.get("eine_ganze_Zahl")):
        return "Fehler: eine_dezimal_Zahl oder eine_ganze_Zahl ist nicht definiert"
    else:
        if local_vars["eine_dezimal_Zahl"] != 0.5:
            return "Fehler: eine_dezimal_Zahl ist nicht 0.5"
        elif local_vars["eine_ganze_Zahl"] != 50:
            return "Fehler: eine_ganze_Zahl ist nicht 50"
        else:
            return "Success"
