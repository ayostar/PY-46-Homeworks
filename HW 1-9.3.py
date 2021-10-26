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