import nltk
import nltk.tag


def detect_answer_type(question):
    tag_question = nltk.pos_tag(question)

    for index in range(0, len(tag_question)):
        word, tag = tag_question[index]

        if tag in ['WP', 'WRB']:

            if word == 'where':
                return 'LOCATION'

            if word == 'when':
                return 'TIME'

            if word in ['who', 'whom', 'whose']:
                return 'PEOPLE'

            if word == 'what':
                if index == len(tag_question) - 1:
                    return 'OTHER'
                else:
                    if tag_question[index + 1][1] == 'NN':
                        if tag_question[index + 1][0] in ['year', 'month', 'day', 'age', 'century', 'time']:
                            return 'TIME'
                        if tag_question[index + 1][0] in ['city', 'street', 'town', 'country', 'state']:
                            return 'LOCATION'
                        if tag_question[index + 1][0] in ['percentage']:
                            return 'NUMBER'
                        if tag_question[index + 1][0] in ['team', 'publication', 'organization', 'company',
                                                          'government', 'university']:
                            return 'ORG'
                    if tag_question[index + 1][1] in ['JJ', 'JJR', 'JJS']:
                        j = index + 1
                        while j < len(tag_question) and tag_question[j][1] != 'NN':
                            j += 1
                        if j < len(tag_question) and tag_question[j][1] != 'NN':
                            if tag_question[j][0] in ['year', 'month', 'day', 'age', 'century', 'time']:
                                return 'TIME'
                            if tag_question[j][0] in ['city', 'street', 'town', 'country', 'state']:
                                return 'LOCATION'
                            if tag_question[j][0] in ['percentage']:
                                return 'NUMBER'
                            if tag_question[j][0] in ['team', 'publication', 'organization', 'company', 'government',
                                                      'university', 'newspaper']:
                                return 'ORG'

        if word == 'which':
            if index == len(tag_question) - 1:
                return 'OTHER'
            else:
                if tag_question[index + 1][0] in ['year', 'month', 'day', 'age', 'century', 'time']:
                    return 'TIME'
                if tag_question[index + 1][0] in ['city', 'street', 'town', 'country', 'state']:
                    return 'LOCATION'
                if tag_question[index + 1][0] in ['team', 'publication', 'organization', 'company', 'government',
                                                  'university', 'newspaper']:
                    return 'ORG'

        if word == 'why':
            return 'OTHER'

        if word == 'how':
            if tag_question[index + 1][0] in ['many', 'much', 'far', 'long', 'old']:
                return 'NUMBER'

    return 'OTHER'
