from datetime import datetime as dt


def parseDatetime(date: dt):
    """
    function to convert datetime object to time format for ics
    :param date: datetime object to be converted
    :return: string formatted to time format for ics (yyyymmddThhmmss)
    """
    return "%4d%02d%02dT%02d%02d%02d" % (date.year, date.month, date.day, date.hour, date.minute, date.second)


class Event:
    """
    Class to handle events for calendar
    """
    def __init__(self):
        self.summary = ""
        self.description = ""
        self.rruleDay = ""
        self.location = ""
        self.uid = ""
        self.created = dt.today()
        self.startTimeStamp = dt(1, 1, 1)
        self.endTimeStamp = dt(1, 1, 1)
        self.rruleEnd = dt(1, 1, 1)

    def getFormatted(self):
        """
        function to format event details to ics format
        :return: ics formatted string containing details of event
        """
        formatted = "" \
                    "BEGIN:VEVENT\n" \
                    "DTSTART;TZID=America/Halifax:{}\n" \
                    "DTEND;TZID=America/Halifax:{}\n" \
                    "RRULE:FREQ=WEEKLY;WKST=SU;UNTIL={};BYDAY={}\n" \
                    "DTSTAMP:{}\n" \
                    "UID:{}\n" \
                    "CREATED:{}\n" \
                    "DESCRIPTION:{}\n" \
                    "LAST-MODIFIED:{}\n" \
                    "LOCATION:{}\n" \
                    "STATUS:CONFIRMED\n" \
                    "SUMMARY:{}\n" \
                    "END:VEVENT\n".format(parseDatetime(self.startTimeStamp), parseDatetime(self.endTimeStamp),
                                          parseDatetime(self.rruleEnd), self.rruleDay,
                                          parseDatetime(self.created), self.uid,
                                          parseDatetime(self.created), self.description,
                                          parseDatetime(self.created), self.location, self.summary)
        return formatted


class Calendar:
    """
    Class to handle calendar (the main point of creating this is to handle timezone and daylight savings
    """
    def __init__(self):
        self.text = [
            "BEGIN:VCALENDAR",
            "BEGIN:VTIMEZONE",
            "TZID:America/Halifax",
            "BEGIN:DAYLIGHT",
            "TZOFFSETFROM:-0400",
            "TZOFFSETTO:-0300",
            "TZNAME:ADT",
            "DTSTART:19700308T020000",
            "RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU",
            "END:DAYLIGHT",
            "BEGIN:STANDARD",
            "TZOFFSETFROM:-0300",
            "TZOFFSETTO:-0400",
            "TZNAME:AST",
            "DTSTART:19701101T020000",
            "RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU",
            "END:STANDARD",
            "END:VTIMEZONE",
            "END:VCALENDAR"
        ]

    def addEvent(self, event:Event):
        """
        function to add event to calendar
        :param event: object of class Event (described above)
        :return: None
        """
        # The event must be inserted before the "END:VCALENDAR" part of the ics file
        self.text.insert(-1, event.getFormatted())

    def writefile(self):
        """
        function to write the calendar and all events to an ics file (saved in current working directory)
        :return: None
        """
        try:
            ics = open("myCourses.ics", "w+")
            ics.write("\n".join(self.text))
            ics.close()
            print("File myCourses.ics created!")
        except:
            print("Failed to write file")
