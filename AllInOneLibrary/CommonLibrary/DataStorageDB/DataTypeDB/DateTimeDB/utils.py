# -*- coding: utf-8 -*-

import datetime
import calendar


from ..location import models as location_models


from . import models


class DateUtils(object):

    """
    get last day of the month
    """
    @staticmethod
    def get_days(year, month):
        if month > 12 or month < 1:
            return False, "", "month must be 1~12"
        value = calendar.monthrange(year, month)[1]
        return True, value, ""

    """
    get start date or end date
    """
    @staticmethod
    def get_start_date_end_date(start_date=None, end_date=None):
        today = datetime.date.today
        if start_date is None and end_date is None:
            start_date = datetime.datetime(year=today().year, month=today().month, day=1)
            flag, day, msg = DateUtils.get_days(year=today().year, month=today().month)
            end_date = datetime.datetime(
                year=today().year,
                month=today().month,
                day=day,
            )
        if start_date is not None and end_date is None:
            flag, day, msg = DateUtils.get_days(year=start_date.year, month=start_date.month)
            end_date = datetime.datetime(
                year=start_date.year,
                month=start_date.month,
                day=day,
            )
        if start_date is None and end_date is not None:
            start_date = datetime.datetime(year=end_date.year, month=end_date.month, day=1)
        return True, [start_date, end_date], ""

    """
    get total month between two dates
    """
    @staticmethod
    def get_different_month_between_date(start_date, end_date):
        flag, [new_start_date, new_end_date], msg = DateUtils.get_start_date_end_date(start_date=start_date, end_date=end_date)
        diff_year = new_end_date.year - new_start_date.year
        diff_month = new_end_date.month - new_start_date.month
        return (diff_year * 12) - diff_month

    """
    get total days from date with month
    """
    @staticmethod
    def count_days(date, duration_month, only_days=True):
        days = 0
        count = 0
        year = date.year
        for x in range(1, duration_month+1):
            next_month = (date.month + x) - (12*count)
            if next_month >= 12:
                year += 1
                count += 1
            flag, day, msg = DateUtils.get_days(year, next_month)
            days += day
        if only_days:
            return days
        else:
            return date + datetime.timedelta(days)

    """
    operation of multiple time
    """
    @staticmethod
    def time_operation(*args):
        get_lists = [x for x in args]
        if get_lists[0] in ('+', '-'):
            operation = get_lists[0]
        else:
            return False, "", "first input must be + or  - "
        amount = 0
        direction = None
        for count, get_list in enumerate(get_lists):
            if type(get_list) != type(datetime.time(second=1)) and count != 0:
                return False, "", "all input must be datetime.time"
            else:
                if count >= 1:
                    if operation == '+':
                        amount += get_list.hour*3600 + get_list.minute*60 + get_list.second
                        direction = 'normal'
                    else:
                        if count == 0:
                            amount = get_list.hour*3600 + get_list.minute*60 + get_list.second
                        else:
                            amount -= get_list.hour*3600 + get_list.minute*60 + get_list.second

                        if amount < 0:
                            direction = 'reverse'
                            amount = -amount
                        elif amount == 0:
                            direction = 'normal'
                        else:
                            direction = 'forward'
        time = str(datetime.timedelta(seconds=amount)).split(':')
        return True, datetime.time(hour=int(time[0]), minute=int(time[1]), second=int(time[2])), direction

    @staticmethod
    def get_date_range(data=None):
        """
        data = {
            'day': utils.day_month_format(day),
            'month': utils.day_month_format(month),
            'year': year,
            'days': days,
            'day1': utils.day_month_format(day1),
            'month1': utils.day_month_format(month1),
            'year1': year1,
            'months': months,
            'years': years,
            'chkEndDate': False if not self.request.GET.get('chkEndDate') else True,
            'rdoType': rdoType,
        }
        """
        today = datetime.datetime.today()
        if not data:
            start_date = datetime.datetime(day=today.day, month=today.month, year=today.year, hour=0, minute=0, second=0)
            end_date = datetime.datetime(day=today.day, month=today.month, year=today.year, hour=today.hour, minute=today.minute, second=today.second)
            return start_date, end_date
        if data['rdoType'] == '2':
            if data['chkEndDate']:
                start_date = datetime.datetime(day=int(data['day']), month=int(data['month']), year=int(data['year']), hour=0, minute=0, second=0)
                end_date = datetime.datetime(day=int(data['day']), month=int(data['month']), year=int(data['year']), hour=23, minute=59, second=59)
            else:
                start_date = datetime.datetime(day=int(data['day']), month=int(data['month']), year=int(data['year']), hour=0, minute=0, second=0)
                end_date = datetime.datetime(day=int(data['day1']), month=int(data['month1']), year=int(data['year1']), hour=23, minute=59, second=59)
        elif data['rdoType'] == '3':
            start_date = datetime.datetime(day=1, month=3, year=2016, hour=0, minute=0, second=0)
            end_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=23, minute=59, second=59)
        elif data['rdoType'] == '5':
            if data['days'] != '0':
                start_day = datetime.datetime.today() - datetime.timedelta(days=int(data['days']))
                if data['days'] == '1':
                    start_date = datetime.datetime(year=start_day.year, month=start_day.month, day=start_day.day, hour=0, minute=0, second=0)
                    end_date = datetime.datetime(year=start_day.year, month=start_day.month, day=start_day.day, hour=23, minute=59, second=59)
                else:
                    start_date = datetime.datetime(year=start_day.year, month=start_day.month, day=start_day.day, hour=0, minute=0, second=0)
                    end_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=23, minute=59, second=59)
            else:
                start_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=0, minute=0, second=0)
                end_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=23, minute=59, second=59)
        elif data['rdoType'] == '6':
            start_date = datetime.datetime(year=today.year, month=int(data['months']), day=1, hour=0, minute=0, second=0)
            end_date = datetime.datetime(year=today.year, month=int(data['months']), day=DateUtils.get_days(year=today.year, month=int(data['months']))[1], hour=23, minute=59, second=59)
        elif data['rdoType'] == '7':
            start_date = datetime.datetime(year=int(data['years']), month=1, day=1, hour=0, minute=0, second=0)
            end_date = datetime.datetime(year=int(data['years']), month=12, day=31, hour=23, minute=59, second=59)
        else:
            start_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=0, minute=0, second=0)
            end_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=23, minute=59, second=59)

        return start_date, end_date


class TimeUtils(object):
    @staticmethod
    def time_operation(start_time, end_time):
        diff = datetime.datetime.combine(datetime.datetime.now(), end_time) - datetime.datetime.combine(datetime.datetime.now(), start_time)
        d = str(diff).split(':')
        return datetime.time(int(d[0]), int(d[1]), int(d[2]))


class HolidayUtils(object):

    @staticmethod
    def get_holiday(date=None, state=None, country=None):
        today = datetime.date.today
        dicts = {}
        get_country = None
        get_state = None
        if country:
            try:
                get_country = location_models.Country.objects.get(name=country)
                dicts.update({'country_id': get_country.id})
            except:
                return False, None, "Country Not Found"

        if state:
            try:
                get_state = location_models.State.objects.get(name=state)
                dicts.update({'state_id': get_state.id})
            except:
                return False, None, "State Not Found"

        if not date:
            date = today
        dicts.update({'date': date})
        try:
            get_holiday = models.Holiday.objects.get(**dicts)
            if get_holiday:
                return True, "", "Holiday on (%s)" % str(date)
        except:
            return False, "", "No Holiday"



