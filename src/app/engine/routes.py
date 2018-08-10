import pandas as pd
import numpy as np

from helpers import utils


def build_route_name(row):
    return '{} - {} ({})'.format(
        row.airportOrigin,
        row.airportDest,
        row.countryDest
    )


def load_international_passengers():
    raw = (
        pd.read_csv(utils.get_raw_file('international-routes-pax.csv'))
        .assign(date = lambda x: pd.to_datetime(x.yearMonth, format='%Y%m', errors='coerce'))
        .assign(regionDest = lambda x: x.regionDest.str.replace('[^a-zA-Z]', ''))
    )
    
    # raw['route'] = raw.apply(build_route_name, axis=1)
    raw['route'] = raw.apply(lambda x: '{} - {} ({})'.format(x.airportOrigin, x.airportDest, x.countryDest), axis=1)
    return raw
