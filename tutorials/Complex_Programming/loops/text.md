# Wiederholungen
Viele Probleme brauchen
die Wiederholung einer Operation
mehrmals.
Zum Beispiel:
Um die Summe aller Elemente
einer Liste auszurechnen
musst du über jedes Element
gehen und es zu einer Variable
addieren.
Dies ist eine Version der
`sum` Funktion:
<pre>
  <code class="python-lang">
def sum(xs): #xs, eine Liste von Nummern
  result = 0
  for x in xs:
    result += x # Das gleiche wie: result = result + x
  return result
  </code>
</pre>
Hier habe ich zwei neue Strukturen benutzt:
<ol>
  <li>Eine Kurzhand für `result = result + x`</li>
  <li>Eine `for` Schleife</li>
</ol>

## Die Kurzhand
Es kommt oft vor, dass du
einer Variable etwas hinzufügst,
wie hier:
<pre>
  <code class="python-lang">
result = result + x
  </code>
</pre>
Es ist das gleiche wie:
<pre>
  <code class="python-lang">
result += x
  </code>
</pre>
Diese Kurzhand gibt es für alle Mathe-Operationen:
<pre>
  <code class="python-lang">
result = 100
result += 2 # 102
result -= 2 # 100
result *= 2 # 200
result **= 2 # 200 ** 2 = 40000
result /= 2 # 20000
result %= 3 # 2
  </code>
</pre>
Sie funktionieren alle gleich.

## Die `for`-Schleife
Die `for`-Schleife gibt es in vielen Programmiersprachen.
Und sie ist die nützlichste der Python Schleifen.
Die Syntax sieht generell so aus:
<pre>
  <code class="python-lang">
for i in Liste:
  code
  </code>
</pre>
Der eingerückte Code wird wiederholt.
Und mit jedem durchlauf ändert sich der Wert
von `i`.
Erst ist `i` `1`,
dann `2` und schließlich `3`.

Nun weißt du wie `sum` funktioniert.
Die Funktion bekommt eine Liste
als Argument.
Und mit geht durch alle Elemente der Liste,
addiert sie zum Ergebnis.

## Die `while`-Schleife
<pre>
  <code class="python-lang">
while Bedingung:
  code
  </code>
</pre>
Die `while`-Schleife wird den
eingerückten Code solange ausführen
bis die Bedingung `False` ist.
Nützlich ist eine `while`-Schleife
zum Beispiel um eine endlose Schleife
zum Programmieren, eine Schleife
die nie endet.
<pre>
  <code class="python-lang">
while True:
  code
  </code>
</pre>
Webserver, Betriebssysteme und
andere Anwendungen die auf Eingaben und
