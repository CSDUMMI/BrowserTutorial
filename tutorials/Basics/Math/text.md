# Rechnungen
Zahlen in Variablen sind schön um sie zu speichern,
aber es ist mindestens genau so wichtig sie verändern zu können

Zum einen kannst du Variablen in Python auch zum Rechnen benutzten.
Es gibt 6 einfache Rechenoperationen:<br>
 `+  : Addition`<br>
 `-  : Subtraktion` <br>
 `*  : Multiplikation` <br>
 `/  : Division` <br>
 `%  : Modulo` <br>
 `** : Exponent` <br>
Die ersten vier sollten einfach zu verstehen sein.
Aber die letzten zwei sind etwas ungewöhnlich.
`12 % 5` gibt `2` zurück, `%` heißt auch Modulo oder Rest Operator.

Wenn du `12 % 5` ausrechnen würdest, beginnst du mit dem zählen, wie oft
`5` in `12` passt, dann die diese Zahl mal `5` nehmen und von `12` abziehen.
Das bedeutet `5` passt `2` mal in `12` ( `10` ) und `2 * 5 = 10`
bedeutet der Rest ist `12 - 10 = 2`.

Der andere Operator den du nicht kennst,
oder die du nicht kennst so wie sie Python schreibt,
ist `**`, der Exponent.
Am besten ich gebe dir also ein Beispiel:
`2 ** 8` ist `2*2*2*2*2*2*2*2`, den `2*` Teil `8` mal.
Allgemein bedeutet, dass der Teil vor dem `**` für so
oft multipliziert wird, wie nach dem `**` gesagt.
Zu dieser Operation sagt man auch `x` hoch `y` wenn `x ** y`
da steht. `x` und `y` sind Variablen.

# Test it
Ich habe eine Variable `site_length` dfiniert, sie stellt
die Seite eines Quadrates dar und du sollst mir die Fläche ausrechnen.
Speichere das Ergebnis in der Variable `area`.
Die Fläche eines Quadrates berechnest du indem du
die Seite mit sich selbst mal nimmst.
Außerdem muss ich wissen ob `site_length` eine gerade oder ungerade Zahl
ist.
Um herraus zu finden ob eine Zahl gerade oder ungerade ist musst du einfach
wissen, ob die Zahl geteilt durch `2` einen Rest hat oder nicht,
speichere also den Rest von `site_length` und `2` in `rest`.
