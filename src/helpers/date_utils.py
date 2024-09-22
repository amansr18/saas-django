import datetime

def timestamp_as_datetime(timestamp):
    ist_offset = datetime.timedelta(hours=5, minutes=30)
    ist_timezone = datetime.timezone(ist_offset)
    return datetime.datetime.fromtimestamp(timestamp, tz=ist_timezone)