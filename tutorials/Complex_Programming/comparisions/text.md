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

# Eine Kombination
Wenn du zum Beispiel testen willst,
ob du etwas kaufen kannst,
nimmst du den Preis und dein Geld
und falls du genauso viel oder mehr
Geld hast, kannst du sie  kaufen.
Da es viele solche Fälle gibt, wo du
testen musst ob etwas gößer oder gleich,
oder kleiner oder gleich ist.
<pre>
  <code class="python-lang">
if geld >= preis:
  kaufen()
  </code>
</pre>
Code für das Beispiel oben,
wenn du mehr oder gleich viel `geld`, wie
`preis`, hast.

Es gibt zwei solche Kombinationen:
<pre>
  <code class="python-lang">
is_greater_than_or_equal = 1 >= 0.5 # True
is_less_than_or_equal = 0.5 <= 1 # True
  </code>
</pre>

## Test it
Du hast eine Online-Umfrage gestartet.
Bei einer Frage gab es zwei Wahlmöglichkeiten:
<ol>
    <li> Für </li>
    <li> Gegen </li>
</ol>
Du definierst eine Funktion namens `analyse`.
Die Funktion nimmt zwei Argumente:
<pre>
    <code class="python-lang">
def analyse(votes_for,votes_against):
    </code>
</pre>
Es gibt zwei mögliche Ergebnisse:
<ol>
    <li> Die Stimmen für gewinnen.</li>
    <li>Die Stimmen gegen gewinnen.</li>
</ol>
Wenn es gleich viele für wie gegen Stimmen gibt,
gewinnen die Gegen.

Die Funktion gibt entweder den String:<br>
`"for"` oder `"against"`
