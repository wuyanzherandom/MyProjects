from django.conf import settings
import datetime


def global_settings(request):
    now = datetime.datetime.now
    # return any necessary values
    context_processors = {

        'CURRENT_DATETIME':
        {
            'year': str(now().year),
            'month': str(now().month),
            'day': str(now().day),
            'hour': str(now().hour),
            'minute': str(now().minute),
        },
        'MONTHS': [
            {
                'name': 'January',
                'value': '01',
            },
            {
                'name': 'February',
                'value': '02',
            },
            {
                'name': 'March',
                'value': '03',
            },
            {
                'name': 'April',
                'value': '04',
            },
            {
                'name': 'May',
                'value': '05',
            },
            {
                'name': 'Jun',
                'value': '06',
            },
            {
                'name': 'July',
                'value': '07',
            },
            {
                'name': 'August',
                'value': '08',
            },
            {
                'name': 'September',
                'value': '09',
            },
            {
                'name': 'October',
                'value': '10',
            },
            {
                'name': 'November',
                'value': '11',
            },
            {
                'name': 'December',
                'value': '12',
            },
        ],
        'YEARS': [
            {
                'name': '2017',
                'value': '2017',
            },
            {
                'name': '2018',
                'value': '2018',
            },
            {
                'name': '2019',
                'value': '2019',
            },
            {
                'name': '2020',
                'value': '2020',
            },
        ]
    }

    return context_processors
