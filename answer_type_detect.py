import nltk

lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()


def detect_answer_type(question):
    num_kw = ['many', 'much', 'amount', 'length', 'time', 'day', 'year', 'decade', 'decades', 'long', 'old',
              'range', 'percent', 'level', 'average', 'population', 'wavelength']
    per_kw = ['who', 'who\'s', 'whom', 'whose', 'person', 'name', 'president']
    loc_kw = ['where', 'place', 'district', 'city', 'country']

    for index in range(0, len(question)):
        word = question[index]
        if word in num_kw:
            return 'NUMBER'
        if word in per_kw:
            return 'PERSON'
        if word in loc_kw:
            return 'LOCATION'
        if index == len(question) - 1:
            return 'OTHER'


