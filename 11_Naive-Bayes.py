# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

corpus = ['Sie bauen Nester an Seen und Teichen.',
          'In den Teichen schwimmen oft viele Enten.',
          'Am Ufer sitzen zwei neugierige Stockenten',
          'Maikäfer waren fast ausgestorben.',
          'Die Weibchen tragen Pollen in die Nester.']

labels = ['ente', 'ente', 'ente', 'keine-ente', 'keine-ente']

# Konvertierung der Textdaten in Frequenzen
vectorizer = CountVectorizer()
corpus_counts = vectorizer.fit_transform(corpus).toarray()

# Modell erstellen und trainieren
model = MultinomialNB()
model.fit(corpus_counts, labels)

# Vorhersage für einen neuen Testsatz
test = ['Nester an Teichen nicht anfassen!']
test = vectorizer.transform(test).toarray()     # Testsatz wird in Frequenzen transformiert

pred = model.predict(test)
print(pred)

scores = model.predict_proba(test)
print(scores)
