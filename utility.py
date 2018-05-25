import json
import nltk
import string

stopwords = set(nltk.corpus.stopwords.words('english'))

punctuations = set(string.punctuation)
stemmer = nltk.stem.PorterStemmer()
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()

documents_json_file_path = 'project_files/documents.json'
test_json_file_path = 'project_files/testing.json'
train_json_file_path = 'project_files/training.json'


def load_json(json_file):
    with open(json_file) as json_data:
        return json.load(json_data)


def get_all_documents():
    return_data = {}
    documents = load_json(documents_json_file_path)
    for a_document in documents:
        docid = a_document['docid']
        text = a_document['text']
        return_data[docid] = text
    return return_data


def get_all_test_questions():
    test_json = load_json(test_json_file_path)
    questions = list()
    for data in test_json:
        question = data['question']
        docid = data['docid']
        tuple = (question, docid)
        questions.append(tuple)
    return questions


def get_all_training_questions():
    json_file = load_json(train_json_file_path)
    return json_file


def lemmatize(word):
    lemma = lemmatizer.lemmatize(word, 'v')
    if lemma == word:
        lemma = lemmatizer.lemmatize(word, 'n')
    return lemma


def process_question(sentence):
    words = []
    sentence = nltk.word_tokenize(sentence)
    for word in sentence:
        if word not in punctuations:
            words.append(lemmatize(word.lower()))
    return words


def tokenize_and_remove_stop_words_for_one_para(para):
    words = []
    para = nltk.word_tokenize(para)
    for word in para:
        word = lemmatize(word.lower())
        if word not in punctuations and word not in stopwords:
            words.append(word)
    return words


def tokenize_and_remove_stop_words_for_paras(doc):
    result = {}
    for index in range(0, len(doc)):
        document = doc[index]
        result[index] = tokenize_and_remove_stop_words_for_one_para(document)
    return result

# json_file = load_json('project_files/testing.json')
#
# words = set()
# other = 0
# grammar = "NP: {<DT>?<JJ>*<NN>}"
# cp = nltk.RegexpParser(grammar)
# for data in json_file:
#     question = pre_process.process_question(data['question'])
#     print(question)
#     grammar = "NP: {<DT>?<JJ>*<NN>}"
#     cp = nltk.RegexpParser(grammar)
#     result = cp.parse(nltk.pos_tag(question))
#     # print(result)
#     # result.draw()
#     print(result.productions())
#
#     print(data['question'])
#     type = answer_type_detect.detect_answer_type(question)
#     if type == 'OTHER':
#         other += 1
#     print(type)
#
# print(other)

# grammar = "NP: {<DT>?<JJ>*<NN>}"
# cp = nltk.RegexpParser(grammar)
# result = cp.parse(sentence)
