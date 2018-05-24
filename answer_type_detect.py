import nltk

lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()


def detect_answer_type(question):
    weights = [0, 0, 0, 0]  # per, loc, num, other
    type = 'OTHER'
    num_kw = {'many', 'much', 'amount', 'length', 'time', 'day', 'year', 'decade', 'decades', 'long', 'old',
              'range', 'percent', 'level', 'average', 'population', 'wavelength'}
    per_kw = {'who', 'who\'s', 'whom', 'whose', 'person', 'name', 'president'}
    loc_kw = {'where', 'place', 'district', 'city', 'country'}

    for word in question:
        if word in per_kw:
            weights[0] += 1
        if word in loc_kw:
            weights[1] += 1
        if word in num_kw:
            weights[2] += 1
        else:
            weights[3] += 1
    index = weights.index(max(weights))
    if index == 0:
        type = 'PERSON'
    if index == 1:
        type = 'LOCATION'
    if index == 2:
        type = 'NUMBER'
    if index == 3:
        type = 'OTHER'
    return type


