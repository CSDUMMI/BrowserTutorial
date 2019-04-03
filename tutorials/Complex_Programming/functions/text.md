# Funktionen
* Funktionen sind Code geschrieben um wiederverwendet zu werden.
* Du kannst einer Funktion Daten geben und sie kann dir Daten zurück geben
* Du kannst sie die Funktion von vielen Orten aus ausführen um Daten zu bekommen

## Syntax
<pre>
  <code class="python-lang">
def foo(x):
  bar(x)
  return x+x
  </code>
</pre>
Um eine Funktion zu definieren brauchst du das
Wort `def`.
Darauf folgt der Name der Funktion,
über den Namen kannst du auf die
Funktion zugreifen und sie ausführen.
Hinter dem Namen kommen die Argumente,
Daten die sich bei jedem ausführen
der Funktion verändern. Nützlich um
eine Funktion zu generalisieren.
Jedes Argument ist eine Variable der du,
in den `()`, Namen geben kannst.
`foo` hat ein Argument names `x`.
`foo` nutzt `x` dreimal, einmal um
es der Funktion `bar` als Argument
zu geben und um einen Wert zurück von der Funktion
zu geben.
*Lies weiter wenn du nicht alles verstehst!*

## Funktion ausführen / aufrufen
Um die Funktion `foo` auszuführen:
<pre>
  <code class="python-lang">
a_var = 123
foo(a_var) # x = a_var
  </code>
</pre>
In diesem Fall wird `foo` ausgeführ
und überall wo `x` in `foo` vorkommt
wird es durch `a_var` ersetzt. Jedoch
nur für diesen aufruf.

# `return` - Rückgabewerte
<pre>
  <code class="python_lang">
a_var = 123
result = foo(a_var) # x = a_var
  </code>
</pre>
Das wichtige an diesem Code ist
die zweite Zeile.
Sie besteht aus zwei Teilen:
<ol>
  <li>Eine Zuweisung der Variable `result`</li>
  <li>Ein Aufruf der Funktion `foo` mit dem Argument `a_var`</li>
</ol>
Um die Zeile auszuführen wird Python erst `foo` ausführen,
es wird `bar` mit `a_var` als Argument ausführen und
dann auf die Zeile mit dem `return` treffen.
Dort wird Python den Wert hinter `return` nehmen
und in der Variable `result` speichern.

## Dictionaries
Programme bestehen aus zwei Dinge:
<ul>
  <li>Code</li>
  <li>Daten</li>
</ul>
Deshalb ist die Hälfte der Python
Programmiersprache über Code und die andere
über Daten und Datenstrukturen.
Es gibt noch eine interessante
Datenstruktur in Python: `dict`.
`dict`s sind so ähnlich wie `list`s.
Bei einer Liste bekommst du
Daten mit einem Index, einer Zahl.
Bei `dict`s bekommst du Daten
mit einem Schlüssel, eine Variable.
<pre>
  <code class="python-lang">
users = {
  "bob": 24,
  "anton": 21
}
  </code>
</pre>
*Ein `dict` namens `users`*<br>
Dieser Code definiert das `dict`
`users`.
Innerhalb der `{}` stehen alle
Schlüssel : Daten Paare,
getrennt mit `,`.
Hier `users` speichert den Namen
des Benutzers und ihr Alter.
Du kannst genauso auf Daten zu einem
Schlüssel zugreifen, wie du auf Daten
zugreifen kannst mit einem Index bei
Listen:
<pre>
  <code class="python-lang">
age_bob = users["bob"]
age_anton = users["anton"]
  </code>
</pre>
`age_bob` hat jetzt den Wert `24`.
Und `age_anton` hat den Wert `21`.
Beide Werte hinter dem Schlüssel
`bob` oder `anton`.

## Test it
*Funktionen werden extrem oft benutzt.*
Viele Bibliotheken, Code den andere Leute schreiben
und du benutzen kannst, haben Funktionen über die du
mit der Bibliothek sprechen kannst.
Die wichtigst Bibliothek in Python ist die
Standard Bibliothek, sie definiert solche Sachen
wie `int`, `float`, `list` und `len` Funktion, so wie
alles was du bis jetzt benutzt hast.
Nehmen wir an du betreibst einen imaginären
Blog.
Nutzer können deine Artikel bewerten,
Kommentare schreiben und einen Daumen
hoch oder runter geben.
Es gibt ein `dict` namens `blog`.
Der `blog` sieht ungefähr so aus:
<pre>
  <code class="python-lang">
blog = {
  "artikel_1": {
      "likes": Daumen hoch für den Artikel,
      "dislikes": Daumen runter,
      "comments": Liste von allen Kommentaren (Strings)
    }
}
  </code>
</pre>
Wie du siehst  ist `blog` ein `dict` mit
anderen `dict`s.
Das ist möglich und manchmal eine gute Idee
und geht auch mit Listen von Listen, ist da jedoch
eine schlechte Idee, meistens.
Jedes `dict` in `blog` wird auf
den Artikel durch den Titel zugegriffen.
Ich möchte jetzt nicht jedes Schlüssel : Daten
Paar durchgehen, deshalb habe ich eine Erklärung schon
geschrieben wo sonst die Daten stehen.

## Die Aufgabe

Du sollst hier eine Funktion beenden:
`like(artikel)`.
`artikel` ist ein Schlüssel in `blog`.
Ich werde dich jetzt noch nicht mit Schlüsseln
testen die es nicht gibt, also musst du
den Schlüssel nicht kontrollieren.
Aber das ist nicht deine Aufgabe,
sie soll das `likes`-Feld um eins erhöhen.
*Feld ist in einem `dict` ist ein Schlüssel:Paar*
`dislike(artikel)` soll das gleiche für
`dislikes` tuen.  
