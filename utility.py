import json
import answer_type_detect
import pre_process
import re
import math

def load_json(json_file):
    with open(json_file) as json_data:
        return json.load(json_data)

json_file=load_json('project_files/testing.json')

for data in json_file:
    question=pre_process.process_question(data['question'],False)
    print(question)
    print(answer_type_detect.detect_answer_type(data['question']))