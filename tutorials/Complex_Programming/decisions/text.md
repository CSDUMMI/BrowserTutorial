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
Jetzt können wir zum ersten mal die Modulo Operation nutzen.
Eine interessante Eigenschaft von Modulo ist, dass der
Rest von `x % 2` Null ist, wenn `x` eine gerade und nicht Null wenn
ungerade.
Ich habe eine `int`-Variable mit dem Namen `num` definiert,
du sollst testen ob `num` eine gerade oder ungerade Zahl ist.
Wenn `num` gerade ist setze `is_even` auf `True`, falls
nicht setze `is_even` auf `False`.
`even` heißt gerade auf Englisch, vieles in Programmierung ist auf
Englisch, gewöhn dich daran.
 
