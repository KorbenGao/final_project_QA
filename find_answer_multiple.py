import utility
import answer_type_detect as atd
import tf_idf
import spacy
from nltk import tokenize
import nltk

nlp = spacy.load('en_core_web_lg')


# nlp = spacy.load('en')


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

        question_type, head_word = atd.detect_answer_type2(utility.process_question(question))

        if len(question_type) > 0:
            answer = list()
            for key_index in range(0, len(key_list)):
                sentence = sentence_list[sim_dic[key_list[key_index]]]
                nps = nlp(sentence)
                ents = [(e.text, e.label_) for e in nps.ents]
                for word, label in ents:
                    if label in question_type:
                        if word not in answer:
                            answer.append(word)
                if key_index >= 2 and len(answer) > 0:
                    break
            if len(answer) == 0:
                sentence = sentence_list[sim_dic[key_list[0]]]
                nps = nlp(sentence)
                ents = [(e.text, e.label_) for e in nps.ents]
                for word, label in ents:
                    if word not in answer:
                        answer.append(word)
        else:
            answer = list()
            sentence = sentence_list[sim_dic[key_list[0]]]
            nps = nlp(sentence)
            ents = [(e.text, e.label_) for e in nps.ents]
            for word, label in ents:
                if word not in answer:
                    answer.append(word)
        if len(answer) == 0:
            sentence = sentence_list[sim_dic[key_list[0]]]
            tag_sentence = nltk.pos_tag(nltk.word_tokenize(sentence))
            for word, tag in tag_sentence:
                if tag in ['NN', 'NNP', 'NNR']:
                    if word not in answer:
                        answer.append(word)
        answer = answer[:5]
        answer_string = " ".join(answer)
        # print(answer_string)
        csv_lines.append((id, answer_string))
        print(num)
        num += 1

print("writing csv...")
utility.csv_write(csv_lines, "result.csv")
print("all done !")
