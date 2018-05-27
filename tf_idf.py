import math
import utility


# calculate term frequency for a term in a paragraph
def term_frequency(term, para):
    termFrequency = 0
    for word in para:
        if term == word:
            termFrequency += 1
    return termFrequency


# calculate how many paragraph contains the term
def term_document_frequency(term, tokenized_documents):
    term_document_frequency = 0
    for index in range(0, len(tokenized_documents)):
        document = tokenized_documents[index]
        if term in document:
            term_document_frequency += 1
    return term_document_frequency


# calculate cosin similarity
def cosin_similarity(vector1, vector2):
    fenzi = 0
    fenmu1 = 0
    fenmu2 = 0
    for index in range(0, len(vector1)):
        fenzi += float(vector1[index]) * vector2[index]
        fenmu1 += float(vector1[index]) * vector1[index]
        fenmu2 += float(vector2[index]) * vector2[index]
    fenmu1 = math.sqrt(float(fenmu1))
    fenmu2 = math.sqrt(float(fenmu2))
    return float(fenzi) / (fenmu1 * fenmu2)


def get_document_question_vectors(document, question_list):
    para_num = len(document)

    tocknized_document = utility.tokenize_and_remove_stop_words_for_paras(document)

    word_set = set()
    for index in range(0, len(tocknized_document)):
        para = tocknized_document[index]
        for word in para:
            word_set.add(word)
    word_list = list(word_set)

    doc_vectors = {}
    for para_index in range(0, len(tocknized_document)):
        para = tocknized_document[para_index]
        tf = {}
        for word_index in range(0, len(word_list)):
            frequency = term_frequency(word_list[word_index], para)
            weight = 0
            if frequency > 0:
                weight = 1 + math.log2(frequency)
            tf[word_index] = weight
        doc_vectors[para_index] = tf

    que_vectors = {}
    for que_index in range(0, len(question_list)):
        question_id, question = question_list[que_index]
        query = utility.tokenize_and_remove_stop_words_for_one_para(question)
        que_vector = {}
        for word_index in range(0, len(word_list)):
            frequency = term_frequency(word_list[word_index], query)
            term_document_frequency_value = term_document_frequency(word_list[word_index], tocknized_document)
            weight = 0
            if frequency > 0:
                weight = math.log2(1 + (float(para_num) / float(term_document_frequency_value)))
            que_vector[word_index] = weight
        que_vectors[que_index] = que_vector

    return (doc_vectors, que_vectors)


def get_best_para_index(doc_vectors, query_vector):
    best_index = 0
    best_sim = cosin_similarity(doc_vectors[0], query_vector)
    for para_index in range(1, len(doc_vectors)):
        cosin_sim = cosin_similarity(doc_vectors[para_index], query_vector)
        if cosin_sim > best_sim:
            best_sim = cosin_sim
            best_index = para_index
    return best_index
