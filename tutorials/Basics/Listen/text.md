# Typen
Auch wenn einzelne Variablen sehr nützlich sind,
musst du manchmal, oft, mehr als eine Information.
Deshalb hat Python sogar mehrer Methoden um Sammlungen von Daten
zu speichern.
Diese Arten nennt man in Python auch `Typen`, der Typ einer
Variable hängt von der Information ab, die in ihr gespeichert wird.
So haben wir schon viele Typen benutzt ohne es zu wissen,
der Type einer Ganzzahl (ohne Nachkommastellen ) ist `int`,
kurz für Integer, Englisch für Ganzzahl.
Und `float` für Zahlen mit Nachkommastellen.
Und `str` für Strings.
Mit diesen Ǹamen kannst du auch eine Variable zu einem anderem Type
umwandeln. Zum Beispiel, du willst die Zahl im String, `"42"` als `int`
haben, dann schreibst du `int("42")` und bekommst `42`.
So geht es auch mit allen anderen Typen, doch es gibt manchmal einige
Regeln, so gibt es einen Fehler wenn du versuchst `int("Hello, World!")`,
und wenn du versuchst `int(1.5)` auszuführen, bekommst du `1`, es wird nicht
gerundet sondern es werden die Nachkommastellen weggenommen.

# Listen
Eine Python Liste sieht so aus:
`xs = [0,0,0.2,4.5]`
`xs` besteht nun aus allen Werten zwischen den eckigen Klammern.
Du kannst auf jedes Element in der Liste so zugreifen wie du es
bei Strings machst, mit `xs[index]` wobei `index` wieder der Index
des Elements ist. Elemente einer Liste können unterschiedliche Typen
haben, wie hier `float` und `int` (`0` und `0.2`).
Du kannst neben einzelnen Elementen einer Liste auch bestimmte Bereiche einer
Liste auswählen und eine neue erstellen.
`ys` ist hier die ersten 3 Elemente von `xs`:
`ys = xs[:3]`, das geht auch anders herum,
hier wäre `ys` alles nach dem 4. Element der Liste:
`ys = xs[3:]`, in beiden Fällen ist das 4. Element nicht in der neuen Liste,
das mit dem Index `3`.

# Test it
In anderen Programmiersprachen haben bestimmte Teile einer
Liste Namen, so gibt es zum Beispiel den `head`,
das erste Element einer Liste, `tail` im Gegensatz ist die gesamte
Liste, außer das erste Element.
Ich habe wieder eine Variable `splitMe` definiert, du sollst
den `head` und `tail` finden und die Werte in den gleichnamige Variablen
zu speichern.
