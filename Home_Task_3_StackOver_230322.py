import requests

from pprint import pprint

import datetime


def search_py_questions(py_tag, num_days):
    params = {}
    end_time_sec = int(datetime.datetime.now().timestamp())
    start_time_sec = end_time_sec - (num_days * 60 * 60 * 24)
    params['fromdate'] = start_time_sec
    params['todate'] = end_time_sec
    params['sort'] = 'creation'
    params['tagged'] = py_tag
    params['site'] = 'stackoverflow'
    response = requests.get('https://api.stackexchange.com/2.3/questions', params)
    pprint(f'Start time: {start_time_sec} ({datetime.datetime.fromtimestamp(start_time_sec)}), end time: {end_time_sec} ({datetime.datetime.fromtimestamp(end_time_sec)}).')
    return response.json()

def quest_tag_output(py_tag, num_days):
    count_question = 0
    for item in search_py_questions(py_tag, num_days).get('items'):
        count_question += 1
        create_date = datetime.datetime.fromtimestamp(item["creation_date"])
        activ_date = datetime.datetime.fromtimestamp(item["last_activity_date"])  
        print(f'QUESTION №{count_question} with tag "python":\nAll tags are: {item["tags"]}\nThe question: {item["title"]}\nThe question id: {item["question_id"]}\nThe creation date: {create_date}, last active: {activ_date}\n', '*'*60)

quest_tag_output('python', 2)