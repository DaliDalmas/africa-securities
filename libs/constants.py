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