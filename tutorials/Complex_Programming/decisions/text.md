# Entweder, oder
Du hast bis jetzt sehr einfache Programme geschrieben,
es wurde eine Zeile Code nach der anderen ausgeführt,
und mag doch eine Zeile die andere beeinflussen,
doch wenn du deinen bisherigen Code zweimal
ausführst kommt immer das gleiche raus.
Nun kommt es jedoch sehr oft vor, dass du
Entscheidungen in deinen Programmen treffen willst,
ob du nun eine Sache oder eine andere Sache tust.
Deshalb gibt es in Python eine einfache Konstruktion,
um das zu schaffen.

## If else
    if x:
      doSomething
    else:
      doSomethingElse
Dieser Code prüft `x` und wenn `x` `True` ist wird der Code
ausgeführt der einen Tab eingeschoben wurde bis zum
`else:`, alles hinter `else` wird ausgeführt wenn `x` `False` ist.
`True` und `False` sind die zwei einzigen Werte des Typen `bool`,
`True` ist Englisch für Wahr und `False` für Falsch.
Der Sinn von `bool` ist genau solche Entscheidungen wie hier zu treffen.

# `bool`, kurz für Boolean
Der Name `bool` aus der Mathematik und wie in der Mathematik, die du kennst,
gibt es auch für `bool` einige Grundlegende Operation auf denen heute alle
Computer aufbauen.
Die einfachste Operation heißt `not`, `not True` gibt `False`, `not False`
gibt `True`.
# Test it 1
Wir werden etwas größeres ausprobieren, ich habe zwei Variablen
definiert, `test_me_1` und `test_me_2`. Ich möchte wissen
welchen Wert beide Variablen haben, wenn sie `True` beide
`True` sind setze die Variable `ergebnis` auf `"Beides Wahr"`.
Wenn einer von beiden `True` ist setze `ergebnis` auf `"Eines Wahr"`,
wenn keiner von beiden `True` ist setze `ergebnis` auf `"Keines Wahr"`
