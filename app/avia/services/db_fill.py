import numpy as np
import pandas as pd

from avia.models import Region, Country, Continent, Municipality, Airport, AirportType


def fill_db_avia_data(file_path: str):
    df = pd.read_csv(file_path, delimiter=',')
    df = df.replace({np.nan: None})
    handbooks = df.dropna()

    AirportType.objects.bulk_create([
        AirportType(
            title=airport_type
        ) for airport_type in set(handbooks['type'])
    ])

    Region.objects.bulk_create([
        Region(
            iso_code=region_code
        ) for region_code in set(handbooks['iso_region'])
    ])

    Country.objects.bulk_create([
        Country(
            iso_code=country_code
        ) for country_code in set(handbooks['iso_country'])
    ])

    Continent.objects.bulk_create([
        Continent(
            title=continent_title
        ) for continent_title in set(handbooks['continent'])
    ])

    Municipality.objects.bulk_create([
        Municipality(
            title=municipality_title
        ) for municipality_title in handbooks['municipality']
    ])

    airport_types = AirportType.objects.values('title', 'id')
    regions = Region.objects.values('iso_code', 'id')
    countries = Country.objects.values('iso_code', 'id')
    continents = Continent.objects.values('title', 'id')
    municipalities = Municipality.objects.values('title', 'id')

    df['type'].replace(to_replace=airport_types, inplace=True)
    df['iso_region'].replace(to_replace=regions, inplace=True)
    df['iso_country'].replace(to_replace=countries, inplace=True)
    df['continent'].replace(to_replace=continents, inplace=True)
    df['municipality'].replace(to_replace=municipalities, inplace=True)

    Airport.objects.bulk_create([
        Airport(
            ident=airport.ident,
            local_code=airport.local_code,
            name=airport.name,
            coordinates=airport.coordinates,
            elevation_ft=airport.elevation_ft,
            gps_code=airport.gps_code,
            iata_code=airport.iata_code,

            continent_id=airport.continent,
            type_id=airport.type,
            country_id=airport.iso_country,
            region_id=airport.iso_region,
            municipality_id=airport.municipality,
        ) for airport in df.itertuples()
    ])
