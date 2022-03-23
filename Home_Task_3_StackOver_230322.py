import requests

import datetime


def search_py_questions(py_tag, num_days=2):
    params = {}
    count_question = 0
    end_time_sec = int(datetime.datetime.now().timestamp())
    start_time_sec = end_time_sec - 172800
    params['previous_day'] = end_time_sec
    params['the_next_day'] = start_time_sec
    params['tagged'] = py_tag
    params['site'] = 'stackoverflow'
    response = requests.get('https://api.stackexchange.com/2.2/questions', params)
    for item in response.json().get('items'):
        count_question += 1
        create_date = datetime.datetime.fromtimestamp(item["creation_date"])
        print(f'QUESTION №{count_question} with tag "python":\nAll tags are: {item["tags"]}\nThe question: {item["title"]}\nThe question id: {item["question_id"]}\nThe creation date: {create_date}\n', '*'*60)

search_py_questions('python', 2)
