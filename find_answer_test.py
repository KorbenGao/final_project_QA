import utility
import answer_type_detect as atd
import tf_idf
import spacy
from nltk import tokenize
import random

# nlp = spacy.load('en_core_web_lg')

documents = utility.get_all_documents()
questions = utility.get_all_test_questions()
json_file = utility.get_all_training_questions()

docid_questions_dic = {}

for data in json_file:
    question = data['question']
    docid = data['docid']
    id = data['answer_paragraph']
    if docid in docid_questions_dic.keys():
        docid_questions_dic[docid].append((id, question))
    else:
        docid_questions_dic[docid] = [(id, question)]

sum = 0
right = 0

for key in docid_questions_dic.keys():
    question_list = docid_questions_dic[key]
    document = documents[key]
    document_vectors, query_vectors = tf_idf.get_document_question_vectors(document, question_list)
    for question_index in range(0, len(question_list)):
        id, question = question_list[question_index]
        query_vector = query_vectors[question_index]
        best_para_index = tf_idf.get_best_para_index(document_vectors, query_vector)
        print("%s---%s" % (id, best_para_index))
        sum += 1
        if id == best_para_index:
            right += 1
        print("[%s] %s" % (sum, float(right) / sum))
