import pandas as pd
import numpy as np
from geopy.distance import geodesic

df = pd.read_csv('201809-citibike-tripdata.csv')
tmp = df[df['start station id'] != df['end station id']]
#df1['distance'] = df1['start station latitude', 'start station longitude', 'end station latitude','end station longitude'].apply(gp.geodesic.km)

tmp['distance'] = tmp.apply(lambda x: geodesic((x['start station latitude'], x['start station longitude']),
                                                            (x['end station latitude'], x['end station longitude'])).km, axis = 1)

print(tmp['distance'].mean()) 