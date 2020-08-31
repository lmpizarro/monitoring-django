from app.models import Meeter, MeetUP
from datetime import datetime, timedelta
import pytz

class Notifications:

    def week_meetups(self):
        # execute on sunday midnight

        now = datetime.now().replace(tzinfo=pytz.UTC)
        endweek = timedelta(days=7)

        meetup_qs = MeetUP.objects.filter(meet_date__gt=now, meet_date_lt=endweek)
        meeters_qs = Meeter.objects.all()

        emails = [meeter.email for meeter in meeters_qs]
        meetups = [meetup.email for meetup in meetup_qs]

        return (emails, meetups)


