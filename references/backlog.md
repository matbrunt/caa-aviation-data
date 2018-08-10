# Project Backlog

## Features

- Get airport lat/long, build route distance

```python
from geopy.distance import vincenty

def route_distance(row):
    origin = (row['o_city_latitude'], row['o_city_longitude'])
    destination = (row['d_city_latitude'], row['d_city_longitude'])
    return vincenty(origin, destination).km

df['flight_distance_km'] = df.apply(route_distance, axis=1)
```

## Data Cleaning Required

- airport names
    - e.g. country FRANCE, airportDest 'VARRY (CHALONS SUR MARNE)' and 'VARY (CHALONS SUR MARNE)'
- what about countries that have changed name?
    - e.g. Bosnia
- up to around 2005, there are a large number of instances of '=' airportDest
- what is 'OTHER ROUTES' origin airport?


## UK CAA Data

- UK to rest of world route analysis

- Passenger numbers

- Aircraft movement data

- Reliability (service on-time) data
