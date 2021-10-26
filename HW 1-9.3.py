from pprint import pprint
from datetime import datetime
from datetime import timedelta
import requests as req


class Stackoverflow:

    def get_questions_wth_tag(self, tag, days):
        url = "https://api.stackexchange.com/2.3/questions"
        dt_temp = datetime.now()
        days = timedelta(days)
        from_date_temp = dt_temp - days
        from_date = from_date_temp.strftime('%Y-%m-%d')
        to_date = dt_temp.strftime('%Y-%m-%d')
        headers = {'Accept': 'application/json'}
        params = {'order': 'desc', 'sort': 'activity', 'site': 'stackoverflow', 'fromdate': from_date, 'todate': to_date, 'tagged': tag, 'filter': 'total'}
        response = req.get(url=url, headers=headers, params=params)
        response_dict = dict(response.json())
        total_number_of_questions = response_dict.get('total')
        return f'Количество запросов с тэгом {tag} составляет: {total_number_of_questions}'
        # list_of_questions = response_dict.get('items')
        # for el in list_of_questions:
        #     print(el.get('tags'))
        # number_of_questions = len(list_of_questions)
        # return f'Количество запросов с тэгом {tag} составляет: {number_of_questions}'


if __name__ == '__main__':
    stack_inquiry = Stackoverflow()
    pprint(stack_inquiry.get_questions_wth_tag('Python', 2))
