from ics import *
import urllib.request
from datetime import datetime, timedelta

url = 'file:///Users/ry/W/giocal/feed.ics'

with urllib.request.urlopen(url) as response:
   ics_string = response.read()

window_start = datetime.now(timezone.utc)
window_end = datetime.now(timezone.utc) + timedelta(days=120)

events = get_events_from_ics(ics_string, window_start, window_end)

for e in events:
    print('{} - {}'.format(e['startdt'], e['summary']))
