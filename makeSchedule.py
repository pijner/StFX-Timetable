from parseFiles import *
from makeICS import Calendar, Event
from datetime import datetime as dt, timedelta

import numpy as np

MY_CAL = Calendar()
MY_SCHEDULE = getSchedule()
COURSES = getCourses()
T1_START_DATE = '14-Sep-2020'
T1_END_DATE = '3-Dec-2020'
T2_START_DATE = '6-Jan-2021'
T2_END_DATE = '8-Apr-2021'


def insertCourse(crn):
    """
    function to insert course into calendar by creating an event
        if a course has n classes per week, each class is created as a separate event recurring weekly
    :param crn: crn (course registration number) of course to be inserted
    :return: None
    """
    thisCourse = COURSES.get(COURSES['CRN'] == crn)
    timeBlock = list(thisCourse['TIMEBLOCK'])[0].split('/')
    if timeBlock == 'TBA':
        print("Skipping course {} since time block is TBA".format(thisCourse['COURSE']))
    if list(thisCourse['TERM'])[0][0] == 'F':
        term = 3
    else:
        term = int(list(thisCourse['TERM'])[0][0])

    for block in timeBlock:
        # Create event for calendar
        thisEvent = Event()
        thisEvent.summary = list(thisCourse['TITLE'])[-1]
        [thisEvent.startTimeStamp, thisEvent.endTimeStamp, day] = getTime(block, term=term)
        thisEvent.rruleEnd = \
            dt.strptime(T1_END_DATE, '%d-%b-%Y') if term == 1 else dt.strptime(T2_END_DATE, '%d-%b-%Y')
        thisEvent.description = list(thisCourse['COURSE'])[-1] + '\\n' \
                                + list(thisCourse['DELIVERY'])[-1] + '\\nProf: ' + list(thisCourse['PROFS'])[-1]
        location = str(list(thisCourse['ROOM'])[-1])
        thisEvent.location = '' if location == 'nan' else location
        thisEvent.uid = 'stfxcourse' + str(crn) + str(block)
        thisEvent.rruleDay = day

        MY_CAL.addEvent(thisEvent)


def getTime(block, term):
    """
    function to get start and end time of a course given a time block and term
    for more information on timeblocks, see
        https://www2.mystfx.ca/sites/mystfx.ca.registrars-office/files/Final_202110%20Adjusted%20Grid%20-%20Updated.pdf
    :param block: string indicating block from StFX's timeblock
    :param term: integer indicating term (1 for term 1, 2 for term 2, 3 for full year)
    :return: list containing start and end time of first class of the course. The times are in datetime format
             list also contains a string containing first two characters of the day of the timeblock
    """
    dayDict = {'MON': 0, 'TUE': 1, 'WED': 2, 'THU': 3, 'FRI': 4}

    time = list(MY_SCHEDULE.iloc[np.where((MY_SCHEDULE == block))[0]]['TIME'])
    day = list(MY_SCHEDULE.columns[np.where((MY_SCHEDULE == block))[1]])[0].split('_')[0]

    startDate = T2_START_DATE if term == 2 else T1_START_DATE
    startTime = dt.strptime(startDate + ' ' + time[0], '%d-%b-%Y %H:%M')
    endTime = dt.strptime(startDate + ' ' + time[-1], '%d-%b-%Y %H:%M')

    delta = timedelta(days=dayDict[day])
    startTime += delta
    endTime += delta

    return [startTime, endTime, day[0:2]]


if __name__ == '__main__':
    while True:
        crn = input("Enter course CRN to add to calendar (enter -1 to exit) ")
        if crn == '-1': break
        insertCourse(int(crn))

    MY_CAL.writefile()
