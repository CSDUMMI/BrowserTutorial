# Funktionen
- Funktionen sind Code geschrieben um wiederverwendet zu werden.
- Du kannst einer Funktion Daten geben und sie kann dir Daten zurück geben
- Du kannst sie die Funktion von vielen Orten aus ausführen um Daten zu bekommen

## Syntax
In Python werden Funktionen so definiert:
    def foo(a,b):
      bar_result = bar(b)
      return a
      
Jede Python Funktion hat drei Teile:
1. Der Kopf der Funktion
Angefangen mit dem Wort `def` und dem Namen der Funktion, `foo`,
hinter dem Namen stehen in Klammern die Argumente für die Funktion.
Du kannst diesen Argumenten hier Namen geben.
Der Kopf der Funktion endet mit `:`
2. Der Körper der Funktion
Hinter dem `:` wird der Körper der Funktionen eingerückt.
Im Code kannst du auf die argumente zugreifen
wir normale Variablen.
Du kannst hier andere Funktionen aufrufen, Variablen definieren,
kurz ganz normalen Code schreiben. Es gibt nur einige wenige
unterschiede zu Code den du in normalen, `global`, Umständen ausführst.
Einer der großen Unterschiede ist, dass du die Variablen in  
einer Funktionen nicht von außen erreichen kannst und normalerweise
auch keine Variablen die außerhalb der Funktion
definert wurden in ihr.
