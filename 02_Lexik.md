# 2. Musterlösung Lexik

1. Zur Tokenisierung stehen die Skripte `02_Tokenisierung-nltk.py`, `02_Tokenisierung-spaCy.py`und 
`02_Tokenisierung-stanza.py` zur Verfügung, die jeweils die im Titel genannte Bibliothek nutzen.

2. Der PMI-Wert für das Wortpaar *der Kuchen* beträgt 5,23, derjenige für das Wortpaar *Kuchen backen* 8,29. 
*Kuchen backen* bildet also eine stärkere Kollokation als *der Kuchen*, obwohl letzteres in absoluten Zahlen häufiger 
vorkommt. Allerdings ist *der* auch alleinstehend schon sehr häufig, sodass auch ein häufigeres Vorkommen der 
Kombination *der Kuchen* zu erwarten ist.

Wortpaar | Erwartete Frequenz |	Quotient |	PMI
:--------|                ---:|     ----:| ---:|
_der Kuchen_	| (50 * 1000) / 75000 = 0,67 |   25 / 0,67 = 37,50 | log(37,50) = 5,23
_Kuchen backen_ | (50 * 120) / 75000 = 0,08 |   25 / 0,08 = 312,50 | log(312,50) = 8,29

3. (keine Musterlösung)