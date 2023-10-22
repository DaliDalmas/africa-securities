from sqlalchemy.types import FLOAT, String, DateTime
securities_data_types = {
    'COMPANY': String(),
    'PRICE': FLOAT(),
    'CHANGE': FLOAT(),
    'VALUE': FLOAT(),
    'VOLUME': FLOAT(),
    'YTD': FLOAT(),
    'SECTOR': String(),
    'UPDATED': DateTime(),
    'country': String(),
    'exchange': String(),
    'fetched_at_utc': DateTime()
}

securities_floating_columns = ['PRICE', 'CHANGE', 'VALUE', 'VOLUME', 'YTD']

jse_data_types = {
    "symbol":String(),
    "name":String(),
    "value":FLOAT(),
    "change":FLOAT(),
    "volume":FLOAT(),
    "high":FLOAT(),
    "low":FLOAT(),
    "country":String(),
    "exchange":String(),
    "fetched_at_utc":DateTime()
}

jse_floating_columns = ["value", "change", "volume", "high", "low"]

rse_data_types = {
    'company':String(),
    'sector':String(),
    'price':FLOAT(),
    '1d':String(),
    'ytd':String(),
    'date':String(),
    'country':String(),
    'exchange':String(),
    'fetched_at_utc':String()
}

rse_floating_columns = [
    "price"
]