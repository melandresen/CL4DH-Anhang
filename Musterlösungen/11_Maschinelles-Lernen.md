# 11. Musterlösung Maschinelles Lernen

1. Überwachtes vs. unüberwachtes Lernen
   - Das Modell soll für ein Bild ausgeben, was dargestellt ist: überwacht
   - Das Modell soll zu einem Gedicht andere, ähnliche Gedichte ausgeben: unüberwacht
   - Das Modell soll Bundestagsreden nach Ähnlichkeit gruppieren: unüberwacht
   - Das Modell soll zu einem Text die verwendete Sprache ausgeben: überwacht

2. Modellrechnung Naive-Bayes
   - Prior Probability "Ente": 3 / 5 = 0,6
   - Prior Probability "keine Ente": 2 / 5 = 0,4
   - Vokabulargröße: 27
   - Korpusgröße "Ente": 20
   - Korpusgröße "keine Ente": 11
   - Relative Frequenzen der im Testsatz vorkommenden Token (mit Smoothing):

   | Token      |    relative Frequenz "Ente" | relative Frequenz "keine Ente" |
   |------------|----------------------------:|-------------------------------:|
   | _Nester_   | (1 + 1) / (20 + 27) = 0,043 |    (1 + 1) / (11 + 27) = 0,053 |
   | _an_       | (1 + 1) / (20 + 27) = 0,043 |    (0 + 1) / (11 + 27) = 0,026 |
   | _Teichen_  | (1 + 1) / (20 + 27) = 0,064 |    (0 + 1) / (11 + 27) = 0,026 |
   | _nicht_    |                           – |                              – |
   | _anfassen_ |                           – |                              – |

   - P(Test|Ente) = 0,6 · 0,043 · 0,043 · 0,064 = 6,93488E-05 = 0,000069
   - P(Test|keine Ente) = 0,4 · 0,053 · 0,026 · 0,026 = 1,45794E-05 = 0,00015
   - Die Wahrscheinlichkeit P(Test|Ente) ist am höchsten, sodass wir den Testsatz
     der Klasse "Ente" zuweisen.

3. Zur Umsetzung der Aufgabe 2 in Python steht das Skript `11_Naive-Bayes.py`
   zur Verfügung.
4. Evaluation
   - Accuracy = (20 + 65) / 100 = 0,85
   - Precision = 20 / 21 = 0,95
   - Recall = 20 / 34 = 0,59
   - F1 = (2 · 0,95 · 0,59) / (0,95 + 0,59) = 0,73
   - Wenn das System eine Nachricht der Klasse "Ente" zuweist, können wir uns
     recht gut darauf verlassen, dass das wirklich so ist. Allerdings müssen wir
     davon ausgehen, dass einige Texte im Korpus von Enten handeln, von unserem
     System aber nicht als solche erkannt werden.
