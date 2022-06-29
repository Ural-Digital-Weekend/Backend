import numpy as np
import pandas as pd

from avia.models import Region, Country, Continent, Municipality, Airport, AirportType


def refill_db_avia_data(file_path: str):
    df = pd.read_csv(file_path, delimiter=',')
    df = df.replace({np.nan: None})

    airports_types = set(df['type']) - set(AirportType.objects.values_list('title', flat=True)) - {None}
    regions = set(df['iso_region']) - set(Region.objects.values_list('iso_code', flat=True)) - {None}
    counties = set(df['iso_country']) - set(Country.objects.values_list('iso_code', flat=True)) - {None}
    continents = set(df['continent']) - set(Continent.objects.values_list('title', flat=True)) - {None}
    municipalities = set(df['municipality']) - set(Municipality.objects.values_list('title', flat=True)) - {None}

    AirportType.objects.bulk_create([
        AirportType(
            title=airport_type
        ) for airport_type in airports_types
    ])

    Region.objects.bulk_create([
        Region(
            iso_code=region_code
        ) for region_code in regions
    ])

    Country.objects.bulk_create([
        Country(
            iso_code=country_code
        ) for country_code in counties
    ])

    Continent.objects.bulk_create([
        Continent(
            title=continent_title
        ) for continent_title in continents
    ])

    Municipality.objects.bulk_create([
        Municipality(
            title=municipality_title
        ) for municipality_title in municipalities
    ])

    airport_types = {**dict(AirportType.objects.values_list('title', 'id')), **{None: None}}
    regions = {**dict(Region.objects.values_list('iso_code', 'id')), **{None: None}}
    countries = {**dict(Country.objects.values_list('iso_code', 'id')), **{None: None}}
    continents = {**dict(Continent.objects.values_list('title', 'id')), **{None: None}}
    municipalities = {**dict(Municipality.objects.values_list('title', 'id')), **{None: None}}

    Airport.objects.all().delete()

    Airport.objects.bulk_create([
        Airport(
            ident=airport.ident,
            local_code=airport.local_code,
            name=airport.name,
            coordinates=airport.coordinates,
            elevation_ft=airport.elevation_ft,
            gps_code=airport.gps_code,
            iata_code=airport.iata_code,

            type_id=airport_types[airport.type],
            region_id=regions[airport.iso_region],
            country_id=countries[airport.iso_country],
            continent_id=continents[airport.continent],
            municipality_id=municipalities[airport.municipality],
        ) for airport in df.itertuples()
    ])
