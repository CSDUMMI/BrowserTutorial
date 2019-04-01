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
<pre>
  <code class="lang-python">
if x:
  doSomething
else:
  doSomethingElse
  </code>
</pre>
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
Um zwei `bool`s zu verknüpfen gibt es zwei andere Operationen,
`and` und `or`.
## `and`
Englisch für "und".
<pre>
  <code class="lang-python">
if x and y:
  # x ist True und y ist True
else:
  # x ist nicht True oder y ist nicht True
  </code>
</pre>
Alles hinter `#` wird von Python ignoriert, damit
kannst du etwas kommentieren. Und das `and` im
`if` prüft, ob beide `bool`s links und rechts vom `and`
`True` sind, und nur dann ist das Ergebnis `True`,
sonst `False`.
## `or`
Englisch für "oder".
<pre>
  <code class="lang-python">
if x or y:
  # x ist True oder y ist True
else:
  # weder x noch y ist True
  </code>
</pre>
`or` ist einfach `True`, falls eine oder beide `bool`s
`True` sind.

# Test it
Du hast ein Spiel geschrieben und du willst
kontrollieren, dass nur Spieler mit einer bestimmten XP
auf ein Level zu greifen. Ich habe zwei Variablen definiert:<br>
`xp` - `int` <br>
`level_num` - `int` <br>
Für jedes Level brauchst du `level_num * 10` `xp`.
Du sollst die Variable `has_enough_xp` definieren, die `True` ist,
wenn `xp` für das Level reicht und wenn nicht setze die Variable
`xp_necessary` auf die benötigte XP für einen Levelaufstieg.
