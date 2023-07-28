# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen
# HINWEIS: Beim ersten Durchlauf muss das Tokenisierungsmodell heruntergeladen werden.
# Dazu das Kommentarzeichen ('# ') am Beginn von Zeile 9 beim ersten Durchlauf entfernen.

import nltk

# nltk.download('punkt')

text = '''Ich habe gerade Frau Dr. Meier getroffen. Das Buch erscheint in dritter Aufl. 
Am Mittwoch fliege ich nach New York. Ich mag z.B. Enten.'''

# Segmentierung in Sätze
sent_tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
sentences = sent_tokenizer.tokenize(text)

# Satzweise Segmentierung in Token
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence, language='german')
    print(tokens)
