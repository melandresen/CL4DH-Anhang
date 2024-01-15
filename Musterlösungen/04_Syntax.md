# 4. Musterlösung Syntax

1. Formale und funktionale Bestimmung von Konstituenten

   a)

   | Konstituente                                                       | Form                | Funktion  |
   |--------------------------------------------------------------------|---------------------|-----------|
   | An einem eiskalten und sehr verschneiten Wintertag vor zwei Jahren | Präpositionalphrase | Adverbial |
   | bin                                                                | Verbalphrase        | Prädikat  |
   | ich                                                                | Nominalphrase       | Subjekt   |
   | im Nymphenburger Park in München                                   | Präpositionalphrase | Adverbial |
   | spazieren gegangen                                                 | Verbalphrase        | Prädikat  |

   b)

   | Konstituente                                   | Form                | Funktion         |
   |------------------------------------------------|---------------------|------------------|
   | Buchweizenmehl                                 | Nominalphrase       |  Akkusativobjekt |
   | bekommt                                        | Verbalphrase        |  Prädikat        |
   | man                                            | Nominalphrase       |  Subjekt         |
   | mittlerweile                                   | Adverbphrase        |  Adverbial       |
   | in allen guten Bio-Supermärkten und Drogerien  | Präpositionalphrase |  Adverbial       |

   c)

   | Konstituente           | Form                 | Funktion                                |
   |------------------------|----------------------|-----------------------------------------|
   | Letztes Jahr im Winter |  Nominalphrase       | Adverbial                               |
   | habe                   | Verbalphrase         | Prädikat                                |
   | ich                    | Nominalphrase        | Subjekt                                 |
   | mich                   | Nominalphrase        | als [Reflexivpronomen](https://grammis.ids-mannheim.de/terminologie/223) Teil des Prädikats |
   | das erste Mal          | Nominalphrase        | Adverbial                               |
   | an Linseneintopf       | Präpositionalphrase  | Präpositionalobjekt                     |
   | gewagt                 | Verbalphrase         | Prädikat                                |

   d)

   | Konstituente                | Form           | Funktion        |
   |-----------------------------|----------------|-----------------|
   | Wir                         | Nominalphrase  | Subjekt         |
   | haben                       | Verbalphrase   | Prädikat        |
   | unserer Experimentierlust   | Nominalphrase  | Dativobjekt     |
   | freien Lauf                 | Nominalphrase  | formal einem Akkusativobjekt ähnlich, bildet hier aber mit *gelassen* ein sog. [Funktionsverbgefüge](https://grammis.ids-mannheim.de/terminologie/85) und ist damit Teil des Prädikats |
   | gelassen                    | Verbalphrase   | Prädikat        |

   e)

   | Konstituente         | Form           | Funktion   |
   |----------------------|----------------|------------|
   | Das heutige Rezept   | Nominalphrase  | Subjekt    |
   | war                  | Verbalphrase   | Prädikat   |
   | absoluter Zufall     | Nominalphrase  | Prädikativ |

2. (keine Musterlösung)

3. Für die Annotation syntaktischer Dependenzen stehen die Skripte
   `04_Dependenzen-spaCy.py` und `04_Dependenzen-stanza.py` zur Verfügung, die
   jeweils die im Titel genannte Bibliothek nutzen.

4. Die Skripte `4_Kontextfreie-Grammatik.py` und
   `04_Kontextfreie-Grammatik-nltk.py` implementieren zwei Varianten einer
   kontextfreien Grammatik. Die Version mit dem NLTK folgt der formalen
   Darstellung im Buch und erlaubt neben der Generierung auch die grammatische
   Analyse von Sätzen. Die zweite Fassung ist eine freie Kombination der
   Grammatikelemente, erlaubt im Gegensatz zur NLTK-Version aber auch die
   randomisierte Generierung von Beispielsätzen, die die Grammatik erlaubt.
