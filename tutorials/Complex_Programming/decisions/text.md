# Entweder, oder
Dein bisheriger Code war bisher sehr linear,
keine Entscheidungen wurden in deinem
Programm getroffen, also etwas in der Art:
Wenn dies, tue das, sonst tue etwas anderes.

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
Das `and` verhält sich ungefähr so: <br>
"Wir können es bezahlen wenn du und ich beide etwas dazu geben".<br>
Nun könnt ihr es nur bezahlen falls du etwas bezahlst und jemand anderes auch.
`and` ist nur `True`, wenn beide `bool`s `True` sind.
Das Beispiel in Python sähe ungefähr so aus:
<pre>
  <code class="python-lang">
if du_bezahlst and er_bezahlt:
  könnt_bezahlen = True
else:
  könnt_bezahlen = False
  </code>
</pre>
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
Wenn du sagst:<br>"Ich komme, wenn du bezahlst oder sie bezahlt",<br>
so kommst du mit
wenn entweder "du" oder "sie" bezahlt, es müssen nicht beide bezahlen sondern
nur einer/eine von beiden.
Genauso funktioniert `or` in Python es ist `True` wenn eine von beiden `bool`s
oder beide `True` sind.
In Code würde das Beispiel so aussehen:
<pre>
 <code class="lang-python">
if du_bezahlst or sie_bezahlst:
  komme_mit = True
else:
  komme_mit = False
 </code>
</pre>
# Test it
Du hast zwei Variablen, die eine Person beschreiben, die `bool`s `has_a_license` und `drives_a_car`,
du willst jetzt kontrollieren, ob die Person eine Straftat begeht indem sie ein Auto fährt.
Eine Person begeht natürlich nur dann eine Straftat, wenn sie Auto fährt **und** **keinen** Führerschein, `has_a_license`
hat.

Wenn die Person ohne Führerschein Auto fährt, setze die Variable `commits_a_crime` auf `True`.
Ansonsten setze sie auf `False`.
