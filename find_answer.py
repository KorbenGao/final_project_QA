import utility
import answer_type_detect as atd
import tf_idf
import spacy
from nltk import tokenize
import random

nlp = spacy.load('en_core_web_lg')


def get_sentence_similarity(question, sentence_list):
    sentenc_sim_dic = {}
    question_ent = nlp(question)
    for sentence_index in range(0, len(sentence_list)):
        sentence = sentence_list[sentence_index]
        sentence_ent = nlp(sentence)
        sim = question_ent.similarity(sentence_ent)
        sentenc_sim_dic[sim] = sentence_index
    return sentenc_sim_dic


documents = utility.get_all_documents()
questions = utility.get_all_test_questions()
docid_questions_dic = {}
for data_index in range(0, len(questions)):
    question = questions[data_index][0]
    docid = questions[data_index][1]
    id = questions[data_index][2]
    if docid in docid_questions_dic.keys():
        docid_questions_dic[docid].append((id, question))
    else:
        docid_questions_dic[docid] = [(id, question)]

csv_lines = []
num = 0
for key in docid_questions_dic.keys():
    question_list = docid_questions_dic[key]
    document = documents[key]
    document_vectors, query_vectors = tf_idf.get_document_question_vectors(document, question_list)

    para_sentences_dic = {}
    for question_index in range(0, len(question_list)):
        id, question = question_list[question_index]
        query_vector = query_vectors[question_index]
        best_para_index = tf_idf.get_best_para_index(document_vectors, query_vector)
        if best_para_index in para_sentences_dic.keys():
            sentence_list = para_sentences_dic[best_para_index]
        else:
            best_para = document[best_para_index]
            sentence_list = tokenize.sent_tokenize(best_para)
            para_sentences_dic[best_para_index] = sentence_list
        sim_dic = get_sentence_similarity(question, sentence_list)
        key_list = list(sim_dic.keys())
        key_list = sorted(key_list, reverse=True)
        key_list = key_list[:5]

        question_type = atd.detect_answer_type(utility.process_question(question))
        answer = 'unknow'
        for key_index in range(0, len(key_list)):
            # print(key_index)
            sentence = sentence_list[sim_dic[key_list[key_index]]]
            nps = nlp(sentence)
            ents = [(e.text, e.label_) for e in nps.ents]
            for word, label in ents:
                if label in question_type:
                    answer = word

        if answer == 'unknow':
            candidates = []
            for index in range(0, len(key_list)):
                sentence = sentence_list[sim_dic[key_list[index]]]
                nps = nlp(sentence)
                ents = [(e.text, e.label_) for e in nps.ents]
                for word, label in ents:
                    candidates.append(word)
            if len(candidates) > 0:
                answer = candidates[random.randint(0, len(candidates)) - 1]

        csv_lines.append((id, answer))
        print(num)
        num += 1
    # break

print("writing csv...")
utility.csv_write(csv_lines, "result.csv")
print("all done !")

# right_num = 0
# sum = 0
#
#
# def get_sentence_similarity(question, sentences):
#     sentenc_sim_dic = {}
#     question_ent = nlp(question)
#     for sentence_index in range(0, len(sentences)):
#         sentence = sentences[sentence_index]
#         sentence_ent = nlp(sentence)
#         sim = question_ent.similarity(sentence_ent)
#         sentenc_sim_dic[sim] = sentence_index
#
#     return sentenc_sim_dic
#
#
# num = 0

# csv_lines = []
#
# for data_index in range(0, len(questions)):
#
#     question = questions[data_index][0]
#     docid = questions[data_index][1]
#     id = questions[data_index][2]
#
#     document = documents[docid]
#     question_type = atd.detect_answer_type(utility.process_question(question))
#     query = utility.tokenize_and_remove_stop_words_for_one_para(question)
#     tockenized_doc = utility.tokenize_and_remove_stop_words_for_paras(document)
#
#     result = tf_idf.tf_idf(query, tockenized_doc)
#     best_index = tf_idf.get_best(result)[0]
#
#     origin_para = document[best_index]
#     sentences = tokenize.sent_tokenize(origin_para)
#
#     sim_dic = get_sentence_similarity(question, sentences)
#     key_list = list(sim_dic.keys())
#     key_list = sorted(key_list, reverse=True)
#     key_list = key_list[:4]
#
#     answer = 'unknow'
#     for key_index in range(0, len(key_list)):
#         # print(key_index)
#         sentence = sentences[sim_dic[key_list[key_index]]]
#         nps = nlp(sentence)
#         ents = [(e.text, e.label_) for e in nps.ents]
#         for word, label in ents:
#             if label in question_type:
#                 answer = word
#
#     if answer == 'unknow':
#         sentence = sentences[sim_dic[key_list[0]]]
#         nps = nlp(sentence)
#         ents = [(e.text, e.label_) for e in nps.ents]
#         candidates = []
#         if len(ents) > 0:
#             if ents[0][1] in ['LOC', 'PRODUCT', 'EVENT', 'ORG', 'PERSON', 'NORP', 'FACILITY', 'GPE', 'WORD_OF_ART',
#                               'LAW', 'LANGUAGE', 'DATE', 'TIME', 'PERCENT', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL']:
#                 candidates.append(ents[0][0])
#         if len(candidates) > 0:
#             answer = candidates[random.randint(0, len(candidates)) - 1]
#
#     csv_lines.append((id, answer))
#     print(num)
#     num += 1
#
# print("writing csv...")
# utility.csv_write(csv_lines, "result.csv")
# print("all done !")
# --------------------------------------------------
# nps = nlp(origin_para)
# ents = [(e.text, e.label_) for e in nps.ents]
#
# print(question_type)
answer = "unknow"
for word, lable in ents:
    # print(word, lable)
    if lable in question_type:
        answer = word
#
