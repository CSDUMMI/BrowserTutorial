# Vergleiche
Neben verknüpfen musst du auch Werte die keine `bool`s sind
Vergleichen können.
In Python kannst du entweder auf Gleichheit, bzw.
Ungleichheit und größer oder kleiner als.

## Gleichheit / Ungleichheit

### Ist gleich
<pre>
  <code class="python-lang">
is_equal = x == y
  </code>
</pre>
`is_equal` ist `True`, wenn `x` und `y` gleich sind.
Zum Beispiel:
<pre>
  <code class="python-lang">
is_equal = 1.0 == 1
  </code>
</pre>
`is_equal` ist jetzt `True`, da du in Python
alle Zahlen mit einander vergleichen kannst.
Neben Zahlen kannst du auch alle anderen Typen
miteinander vergleichen, jedoch nicht unbedingt
mit einer Variable eines anderen Typen.

### ist ungleich
Das Gegenteil von `==` ist `!=`,
ungleich, alles was `True` ist bei `==`,
ist `False` bei `!=`, ansonsten gelten
die gleichen Regeln wie bei `==`.
<pre>
  <code class="python-lang">
is_unequal = 1 != 1 # False
  </code>
</pre>

# Größer als, kleiner als
Wenn du Zahlen vergleichst, kannst du auch testen,
ob eine Zahl größer ist als eine andere, oder kleiner.
<pre>
  <code class="python-lang">
is_greater_than = 1 > 0.5 # True
is_less_than = 1 <  2 # True
is_not_less_than = 1 < 0.5 # False
is_not_greater_than = 1 > 2 # False
  </code>
</pre>

# Test it
Du hast ein Spiel entwickelt, wo jeder
Spieler ein `level` hat und `xp`, beides
`int` Werte.
Wenn nun ein Spieler eine bestimmte Anzahl an XP hat
kommt er zum nächsten Level.
Die Variablen die ich schon definiert habe sind:<br>
`level` Level Nummer des Spielers <br>
`xp` XP des Spielers <br>
`level_threshhold` XP die ein Spieler fürs nächste Level braucht.<br>
Hier sollst du jetzt nicht neue Variablen definieren,
sondern alte verändern.
Die Aufgabe ist einfach:
1. Kontrolliere, ob der Spieler ein neues Level erreicht hat
2. Wenn ja setze die `xp` auf `0` und erhöhe `level`
3. Wenn nicht, tue nichts.
