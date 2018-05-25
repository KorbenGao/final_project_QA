import math


def tf_idf(query, tocknized_document):
    sentence_num = len(tocknized_document)
    word_set = set()
    for index in range(0, len(tocknized_document)):
        sentence = tocknized_document[index]
        for word in sentence:
            word_set.add(word)
    word_list = list(word_set)

    doc_vecctors = {}
    for sentence_index in range(0, len(tocknized_document)):
        sentence = tocknized_document[sentence_index]
        tf = {}
        for word_index in range(0, len(word_list)):
            frequency = term_frequency(word_list[word_index], sentence)
            weight = 0
            if frequency > 0:
                weight = 1 + math.log2(frequency)
            tf[word_index] = weight
        doc_vecctors[sentence_index] = tf

    que_vector = {}
    for word_index in range(0, len(word_list)):
        frequency = term_frequency(word_list[word_index], query)
        term_document_frequency_value = term_document_frequency(word_list[word_index], tocknized_document)
        weight = 0
        if frequency > 0:
            weight = math.log2(1 + (float(sentence_num) / float(term_document_frequency_value)))
        que_vector[word_index] = weight

    result = {}
    for index in range(0, len(tocknized_document)):
        result[index] = cosin_similarity(que_vector, doc_vecctors[index])

    return result


def get_best(result):
    best_result = result[0]
    best_index = 0
    for index in range(1, len(result)):
        if result[index] > best_result:
            best_result = result[index]
            best_index = index
    return best_index, best_result


def term_frequency(term, sentence):
    termFrequency = 0
    for word in sentence:
        if term == word:
            termFrequency += 1
    return termFrequency


def term_document_frequency(term, tokenized_documents):
    term_document_frequency = 0
    for index in range(0, len(tokenized_documents)):
        document = tokenized_documents[index]
        if term in document:
            term_document_frequency += 1
    return term_document_frequency


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
