from datetime import datetime as dt
from typing import Optional


def timestamp_to_datetime(timestamp: Optional[str]) -> Optional[dt]:
    '''Parse timestamp with format YYYY-MM-DDThh:mm:ssZ to datetime'''

    if timestamp is None:
        return None
    date_object = dt.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
    return date_object
