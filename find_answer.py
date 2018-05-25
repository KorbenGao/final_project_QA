import utility
import answer_type_detect as atd
import tf_idf

documents = utility.get_all_documents()
# questions = utility.get_all_test_questions()
json_file = utility.get_all_training_questions()

right_num = 0

for data in json_file:
    question = data['question']
    answer_para = data['answer_paragraph']
    docid = data['docid']
    document = documents[docid]
    question_type = atd.detect_answer_type(utility.process_question(question))
    query = utility.tokenize_and_remove_stop_words_for_one_para(question)
    tockenized_doc = utility.tokenize_and_remove_stop_words_for_paras(document)

    result = tf_idf.tf_idf(query, tockenized_doc)
    best_index = tf_idf.get_best(result)[0]
    print(question)
    print("[right:%s],[our:%s]" % (answer_para, best_index))
    if answer_para == best_index:
        right_num += 1

print("right number: %s" % (right_num))
