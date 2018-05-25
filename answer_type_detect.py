import nltk
import nltk.tag


def detect_answer_type(question):
    tag_question = nltk.pos_tag(question)
    result = set()

    for index in range(0, len(tag_question)):
        word, tag = tag_question[index]

        if word == 'where':
            result.add('LOC')
            result.add('GPE')

        if word == 'when':
            result.add('TIME')
            result.add('DATE')

        if word in ['who', 'whom', 'whose']:
            result.add('PERSON')

        if word == 'what':
            if index == len(tag_question) - 1:
                # return 'OTHER'
                pass
            else:
                if tag_question[index + 1][1] == 'NN':
                    if tag_question[index + 1][0] in ['year', 'month', 'day', 'age', 'century', 'time']:
                        result.add('TIME')
                        result.add('DATE')
                    if tag_question[index + 1][0] in ['city', 'street', 'town', 'country', 'state']:
                        result.add('LOC')
                        result.add('GPE')
                    if tag_question[index + 1][0] in ['percentage']:
                        result.add('PERCENT')
                        result.add('CARDINAL')
                    if tag_question[index + 1][0] in ['team', 'publication', 'organization', 'company',
                                                      'government', 'university']:
                        result.add('ORG')
                if tag_question[index + 1][1] in ['JJ', 'JJR', 'JJS']:
                    j = index + 1
                    while j < len(tag_question) and tag_question[j][1] != 'NN':
                        j += 1
                    if j < len(tag_question) and tag_question[j][1] != 'NN':
                        if tag_question[j][0] in ['year', 'month', 'day', 'age', 'century', 'time']:
                            result.add('DATE')
                            result.add('TIME')
                        if tag_question[j][0] in ['city', 'street', 'town', 'country', 'state']:
                            result.add('LOC')
                            result.add('GPE')
                        if tag_question[j][0] in ['percentage']:
                            result.add('PERCENT')
                            result.add('CARDINAL')
                        if tag_question[j][0] in ['team', 'publication', 'organization', 'company', 'government',
                                                  'university', 'newspaper']:
                            result.add('ORG')

        if word == 'which':
            if index == len(tag_question) - 1:
                # return 'OTHER'
                pass
            else:
                if tag_question[index + 1][0] in ['year', 'month', 'day', 'age', 'century', 'time']:
                    result.add('DATE')
                    result.add('TIME')
                if tag_question[index + 1][0] in ['city', 'street', 'town', 'country', 'state']:
                    result.add('LOC')
                    result.add('GPE')
                if tag_question[index + 1][0] in ['team', 'publication', 'organization', 'company', 'government',
                                                  'university', 'newspaper']:
                    result.add('ORG')

        if word == 'why':
            # return 'OTHER'
            pass

        if word == 'how':
            if tag_question[index + 1][0] in ['many', 'far', 'long', 'old']:
                result.add('DATE')
                result.add('TIME')
                result.add('CARDINAL')
                result.add('QUANTITY')
                result.add('PERCENT')
            if tag_question[index + 1][0] in ['much']:
                if index + 2 < len(tag_question) and tag_question[index + 2][0] in ['money']:
                    result.add('MONEY')
                else:
                    result.add('MONEY')
                    result.add('CARDINAL')
                    result.add('QUANTITY')
    return result


def detect_answer_type2(question):
    tag_question = nltk.pos_tag(question)
    result = set()

    for index in range(0, len(tag_question)):
        word, tag = tag_question[index]

        if word == 'where':
            result.add('LOC')
            result.add('GPE')

        if word == 'when':
            result.add('TIME')
            result.add('DATE')

        if word in ['who', 'whom', 'whose']:
            result.add('PERSON')

        if word == 'what':
            if index == len(tag_question) - 1:
                # return 'OTHER'
                pass
            else:
                if tag_question[index + 1][1] == 'NN':
                    if tag_question[index + 1][0] in ['year', 'month', 'day', 'age', 'century', 'time']:
                        result.add('TIME')
                        result.add('DATE')
                    if tag_question[index + 1][0] in ['city', 'street', 'town', 'country', 'state']:
                        result.add('LOC')
                        result.add('GPE')
                    if tag_question[index + 1][0] in ['percentage']:
                        result.add('PERCENT')
                        result.add('CARDINAL')
                    if tag_question[index + 1][0] in ['team', 'publication', 'organization', 'company',
                                                      'government', 'university']:
                        result.add('ORG')
                if tag_question[index + 1][1] in ['JJ', 'JJR', 'JJS']:
                    j = index + 1
                    while j < len(tag_question) and tag_question[j][1] != 'NN':
                        j += 1
                    if j < len(tag_question) and tag_question[j][1] != 'NN':
                        if tag_question[j][0] in ['year', 'month', 'day', 'age', 'century', 'time']:
                            result.add('DATE')
                            result.add('TIME')
                        if tag_question[j][0] in ['city', 'street', 'town', 'country', 'state']:
                            result.add('LOC')
                            result.add('GPE')
                        if tag_question[j][0] in ['percentage']:
                            result.add('PERCENT')
                            result.add('CARDINAL')
                        if tag_question[j][0] in ['team', 'publication', 'organization', 'company', 'government',
                                                  'university', 'newspaper']:
                            result.add('ORG')

        if word == 'which':
            if index == len(tag_question) - 1:
                # return 'OTHER'
                pass
            else:
                if tag_question[index + 1][0] in ['year', 'month', 'day', 'age', 'century', 'time']:
                    result.add('DATE')
                    result.add('TIME')
                if tag_question[index + 1][0] in ['city', 'street', 'town', 'country', 'state']:
                    result.add('LOC')
                    result.add('GPE')
                if tag_question[index + 1][0] in ['team', 'publication', 'organization', 'company', 'government',
                                                  'university', 'newspaper']:
                    result.add('ORG')

        if word == 'why':
            # return 'OTHER'
            pass

        if word == 'how':
            if tag_question[index + 1][0] in ['many', 'far', 'long', 'old']:
                result.add('DATE')
                result.add('TIME')
                result.add('CARDINAL')
                result.add('QUANTITY')
                result.add('PERCENT')
            if tag_question[index + 1][0] in ['much']:
                if index + 2 < len(tag_question) and tag_question[index + 2][0] in ['money']:
                    result.add('MONEY')
                else:
                    result.add('MONEY')
                    result.add('CARDINAL')
                    result.add('QUANTITY')
    return result
