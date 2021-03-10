"""Markdown Calendar Generator"""
import calendar
from datetime import datetime, date
import sys


def create_calendar(year, month, with_isoweek=False, start_from_Sun=False, add_links=True, lang="en"):
    firstweekday = 6 if start_from_Sun else 0

    cal = calendar.TextCalendar(firstweekday=firstweekday)

    today = date.today()
    

    # Only cross out days for printing out calendar of the current month
    if (today.month == month and today.year == year):
        cross_out_day = True
    else:
        cross_out_day = False

    mdstr = ""
    dic = get_dict(lang)

    colnames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if start_from_Sun:
        colnames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # if with_isoweek:
    #     colnames.insert(0, "Week")
    colnames = [dic[col] for col in colnames]

    mdstr += '|' + '|'.join(colnames) + '|' + '\n'
    mdstr += '|' + '|'.join([':-:' for _ in range(len(colnames))]) + '|' + '\n'

    for days in cal.monthdatescalendar(year, month):


        # if with_isoweek:
        #     isoweek = days[0].isocalendar()[1]
        #     mdstr += '|' + str(isoweek) + '|' + \
        #         '|'.join([f"~~{str(d.day)}~~" if (cross_out_day and d < today) else str(d.day) for d in days]) \
        #         + '|' + '\n'

        # Add links to anchors for each day, for example "<a name="5_25"></a> May 25" 
        if add_links:   
            mdstr += '|' + '|'.join([
                    f"[~~{str(d.day)}~~](#{d.month}_{d.day})" if (cross_out_day and d < today) 
                        else f"[{str(d.day)}](#{d.month}_{d.day})" for d in days
                ]) + '|' + '\n'
        else:

            mdstr += '|' + '|'.join([
                    f"~~{str(d.day)}~~" if (cross_out_day and d < today) else str(d.day) for d in days
                ]) + '|' + '\n'



    ### 
    return mdstr


def print_calendar(year, month, with_isoweek=False, start_from_Sun=False, lang="en"):
    print('{}/{}\n'.format(year, month))
    print(create_calendar(year, month, with_isoweek, start_from_Sun, lang))


def get_dict(lang='en'):
    dic = {}
    colnames = ['Week', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    colnames_zh = ['周', '一', '二', '三', '四', '五', '六', '日']
    if lang == 'en':
        for col in colnames:
            dic[col] = col
    elif lang == 'zh':
        for col, colja in zip(colnames, colnames_ja):
            dic[col] = colja
    else:
        for col in colnames:
            dic[col] = col
    return dic


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 1:
        today = datetime.now()
        print_calendar(today.year, today.month)
    elif len(argv) == 2:
        year = int(argv[1])
        for month in range(1, 13):
            print_calendar(year, month, with_isoweek=True)
    elif len(argv) == 3:
        year, month = [int(a) for a in argv[1:3]]
        print_calendar(year, month)
    else:
        print('Usage: python mdcal.py [year] [month]')