#https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
tracks = pd.read_csv('Moststreamed.csv')



most = tracks.query('popularity > 85', inplace = False).sort_values('popularity', ascending = False)

print(most['artist'])



with open('Topartists.txt', 'w') as f:
    f.write(str(most['artist']))

