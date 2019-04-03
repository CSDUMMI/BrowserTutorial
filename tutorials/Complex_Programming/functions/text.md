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

## Test it
Funktionen werden extrem oft benutzt.
