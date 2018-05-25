import utility
import answer_type_detect as atd
import tf_idf
import spacy

nlp = spacy.load('en_core_web_sm')
# doc = nlp('The cat and the dog sleep in the basket near the door.')
# for np in doc.noun_chunks:
#     print(np)

documents = utility.get_all_documents()
# questions = utility.get_all_test_questions()
json_file = utility.get_all_training_questions()

right_num = 0
sum = 0

for data in json_file:
    question = data['question']
    answer_para = data['answer_paragraph']
    right_answer = data['text']
    docid = data['docid']
    document = documents[docid]
    question_type = atd.detect_answer_type(utility.process_question(question))
    query = utility.tokenize_and_remove_stop_words_for_one_para(question)
    tockenized_doc = utility.tokenize_and_remove_stop_words_for_paras(document)

    result = tf_idf.tf_idf(query, tockenized_doc)
    best_index = tf_idf.get_best(result)[0]
    # print(question)
    # print("[right:%s],[our:%s]" % (answer_para, best_index))
    if answer_para == best_index:
        right_num += 1
    sum += 1

    origin_para = document[best_index]
    nps = nlp(origin_para)
    ents = [(e.text, e.label_) for e in nps.ents]

    # print(question_type)
    answer = "unknow"
    for word, lable in ents:
        # print(word, lable)
        if lable in question_type:
            answer = word

    print("%s --- %s" % (right_answer, answer))
    print()
