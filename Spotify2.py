
import numpy as np
import pandas as pd
tracks = pd.read_csv('Moststreamed.csv')




if tracks['artist'].str.contains('Harry').any():
   print ("Harry is there")

filter = (tracks['artist'].where(tracks['popularity'] > 50))
print(filter)

