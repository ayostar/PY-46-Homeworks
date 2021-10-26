from pprint import pprint
from datetime import datetime
import requests as req


class Stackoverflow:

    def print_questions_wth_tag(self, tag, days):
        url = "https://api.stackexchange.com/2.3/questions"
        date_now = datetime.now()
        to_date = int(datetime.timestamp(date_now))
        from_date = to_date - days * 24 * 60 * 60
        page_count = 1
        question_count = 0
        headers = {'Accept': 'application/json'}
        params = {'order': 'desc', 'sort': 'activity', 'site': 'stackoverflow',
                  'fromdate': from_date, 'tagged': tag,
                  'pagesize': 100}
        proceed = True
        while proceed:
            params['page'] = page_count
            response = req.get(url=url, headers=headers, params=params)
            response_dict = dict(response.json())
            proceed = response_dict.get('has_more')
            list_of_questions = response_dict.get('items')
            page_count += 1
            for el in list_of_questions:
                question_count += 1
                question = el.get('title')
                pprint(f'Вопрос {question_count} с тэгом {tag}: {question}')


if __name__ == '__main__':
    stack_inquiry = Stackoverflow()
    stack_inquiry.print_questions_wth_tag('Python', 2)


#     def get_questions_wth_tag(self, tag, days):
#         url = "https://api.stackexchange.com/2.3/questions"
#         dt_temp = datetime.now()
#         days = timedelta(days)
#         from_date_temp = dt_temp - days
#         from_date = from_date_temp.strftime('%Y-%m-%d')
#         to_date = dt_temp.strftime('%Y-%m-%d')
#         headers = {'Accept': 'application/json'}
#         params = {'order': 'desc', 'sort': 'activity', 'site': 'stackoverflow', 'fromdate': from_date, 'todate': to_date, 'tagged': tag, 'filter': 'total'}
#         response = req.get(url=url, headers=headers, params=params)
#         response_dict = dict(response.json())
#         total_number_of_questions = response_dict.get('total')
#         return f'Количество вопросов с тэгом {tag} составляет: {total_number_of_questions}'
#         # list_of_questions = response_dict.get('items')
#         # for el in list_of_questions:
#         #     print(el.get('tags'))
#         # number_of_questions = len(list_of_questions)
#         # return f'Количество запросов с тэгом {tag} составляет: {number_of_questions}'
#
#
# if __name__ == '__main__':
#     stack_inquiry = Stackoverflow()
#     pprint(stack_inquiry.get_questions_wth_tag('Python', 2))