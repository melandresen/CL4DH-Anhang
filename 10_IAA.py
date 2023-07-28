# Dieses Skript gehört zum digitalen Anhang des Buches "Computerlinguistische Methoden für die Digital Humanities"
# https://www.narr.de/computerlinguistische-methoden-f%C3%BCr-die-digital-humanities-18579-1/
# Autorin: Melanie Andresen

import pandas as pd
from sklearn.metrics import cohen_kappa_score

# Erstellung des Datensatzes
df = pd.DataFrame({'Person-1': 60*['Ente'] + 15*['Ente'] + 10*['Gans'] + 15*['Gans'],
                   'Person-2': 60*['Ente'] + 15*['Gans'] + 10*['Ente'] + 15*['Gans']
                   })

print(df)

# Berechnung und Ausgabe des Inter-Annotator-Agreements
iaa = cohen_kappa_score(df['Person-1'], df['Person-2'])
print(round(iaa, 3))
