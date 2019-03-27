# Variablen 2
Variablen speichern Werte und diese Werte sind über den Namen der Variable
erreichbar und du kannst sie mit dem Namen verändern.
Es gibt noch andere Wege wie wir Zahlen in Variablen verändern,
vorallem Fälle die oft aufkommen:
Die Variable `x` kann mit `x =` auf den Wert rechts vom `=` setzen.
Wenn du eine Zahl in `x` hast, so kommt es vor, dass du zu dieser
Zahl etwas hinzufügts oder abziehst:
`x = x + 1` fügt `1` zu `x` hinzu.
Das kann abgekürzt werden mit:
`x += 1`
`x = x - 1` zieht `1` von `x` ab.
Und kann auch mit `x -= 1` abgekürzt werden.

# Etwas anderes als Zahlen
Auch wenn Computer eigentlich nur mit Zahlen arbeiten,
können sie mithilfe der Zahlen auch andere Daten speichern,
zum Beispiel Buchstaben, oder mehrer Buchstaben, sogenannte Strings.
Ein String in Python wird in etwa so geschrieben:
`"Hello, World!"`, der String speichert nun die Zeichenkette `Hello, World!`.
In Variablen kannst du String genauso speichern wie Zahlen,
Strings haben nur noch einige interessante andere Eigenschaften.
So kannst du etwa einen String an einen anderen anfügen und so einen
neuen erschaffen, nach
`x = "Hello," + " World!"`
hat `x` den Wert `"Hello, World!"`.
Man kann jedoch nicht einfach Zeichen vom Ende abziehen mit `-`.
Wenn du auf ein bestimmtes Zeichen in einem String, sagen wir das
`5.` Zeichen, zugreifen möchtest benutzt du `x[4]`.
Jedes Zeichen in einem String hat einen Index, doch anders als
du es im ersten Moment annehmen wirst hat das erste Zeichen nicht
beim Index `1` sonder beim Index `0`. Im allgemeinen fangen alle
Index in der Informatik mit `0` an.

# Test it
Wir haben schon einen String definiert namens `message`,
nun sollst du uns bestimmte Teile dieses Strings geben:
Speichere die `4.` Stelle in der Variable `char_4`.
`char` ist Englisch für Zeichen, Buchstabe.
Speichere die `2.` Stelle in der Variable `char_2`.
Denk dran, das erste Zeichen in einem String hat den Index `0`.
Und wenn du einen Index angibst der außerhalb von `message` ist bekommst
du eine Fehlermeldung von Python,
ungefähr so:  `string index out of range`
