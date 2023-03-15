import datetime
from datetime import datetime


def get_current_time():
    current_time = datetime.now().replace(microsecond=0)
    return str(current_time)