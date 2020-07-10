import pandas as pd


def getCourses():
    """
    function to read courses.csv
    :return: dataframe of courses,
        columns: CRN, COURSE, COLL, CRED, DELIVERY, TITLE, PROFS, TERM, TIMEBLOCK, ROOM
    """
    courses = pd.read_csv('courses.csv')
    return courses


def getSchedule():
    """
    function to read blank schedule template (for year 2020-2021)
    :return: dataframe of timeblocks
    """
    schedule = pd.read_csv('schedule.csv')
    return schedule
