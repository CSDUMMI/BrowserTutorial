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

# Test it
Du hast ein Spiel programmiert.
In dem kann jeder Spieler XP sammeln
und wenn er eine Schwelle, `xp_threshhold`,
erreicht steigt er im Level auf.
Du sollst die Funktion `gather_xp`
definieren.
Der Funktionskopf sieht so aus:
<pre>
  <code class="python-lang">
def gather_xp(new_xp,player_xp,player_level,level_threshhold):
  </code>
</pre>
`new_xp` ist die Zahl der XP die der Spieler sammelte.<br>
`player_xp` ist die Anzahl der schon gesammelte XP der Spieler.<br>
`player_level` ist die Level Nummer des Spielers.<br>
`level_threshhold` ist die XP die der Spieler braucht um das nächste Level zu erreichen.<br>
Die Regeln für die `gather_xp` Funktion sind:
<ol>
  <li>Ein `player_xp` muss bei `new_xp` erhöht</li>
  <li>Der Spieler soll im Level aufsteigen, wenn `player_xp >= level_threshhold`</li>
  <li> Keine XP gehen verloren. </li>
  <li> Wenn der Spieler noch mehr XP als `level_threshhold` hat bekommt er diese fürs nächste Level</li>
  <li> Wenn er so viel XP kriegt um zwei oder drei oder vier oder usw. Level aufzusteigen, soll er das tuen.</li>
</ol>
*Hilfe zum letzten Punkt: Funktion können sich selbst aufrufen.*

`gather_xp` soll ein `dict` mit drei Feldern zurückgeben
<pre>
  <code class="python-lang">
return {
  "player_level": Neues Level des Spielers,
  "player_xp": Neue XP des Spielers,
  "level_threshhold": Bleibt gleich wie level_threshhold, das Argument
}
  </code>
</pre>
