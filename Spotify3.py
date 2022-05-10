
import numpy as np
import pandas as pd
tracks = pd.read_csv('Moststreamed.csv')




#if tracks['artist'].str.contains('Harry').any():
   #print ("Harry is there")

#def strfinder(tracks, mystr):
    #for col in tracks:
        #for item in tracks[col]:
            #if mystr in item:
                #return col

#print(strfinder(tracks, 'Harry'))
#print(strfinder(tracks, 'electropop'))

#filter = (tracks['artist'].where(tracks['popularity'] > 50))
#print(filter)


#here we can count the number of distinct users viewing on a given day
#new_df = tracks[tracks['artist'].str.contains('Harry')]
#new_df = tracks[tracks['artist'].str.contains('Harry', na=False)]
#print(tracks.head())
