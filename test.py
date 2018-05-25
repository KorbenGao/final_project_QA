import utility
import tf_idf
import spacy
from nltk import tokenize
import random

nlp = spacy.load('en_core_web_lg')

questions = utility.get_all_test_questions()

sum = 0
have = 0

for data_index in range(0, len(questions)):
    question = questions[data_index][0]
    docid = questions[data_index][1]
    id = questions[data_index][2]

    nps = nlp(question)
    ents = [(e.text, e.label_) for e in nps.ents]
    print(question)
    print(ents)
    print()
    sum += 1
    if len(ents) > 0:
        have += 1

print(sum)
print(have)


def process(sentence):
    wh_word_ = ''
    wh_pos_ = ''
    wh_nbor_pos_ = ''
    root_tag_ = ''
    doc = nlp(sentence.lower())
    sent_list = list(doc.sents)
    sent = sent_list[0]
    found = False
    for token in sent:
        if found == False:
            if (token.tag_ in ('MD', 'VBZ', 'VBP')
                    and token.i == 0) or token.tag_ in ('WP', 'WDT', 'WP$',
                                                        'WRB'):
                wh_word_ = token.text
                wh_pos_ = token.tag_
                wh_nbor_pos_ = sent[token.i + 1].tag_
                found = True
            if token.i - 1 >= 0 and token.i + 1 < len(sent):
                if (sent[token.i - 1].dep_ in ('punct')
                        and sent[token.i].tag_ in ('VBZ', 'MD', 'VBP')):
                    wh_word_ = token.text
                    wh_pos_ = token.tag_
                    wh_nbor_pos_ = sent[token.i + 1].tag_
                    found = True
        if token.dep_ == 'ROOT':
            root_tag_ = token.tag_
    if found == False:
        wh_word_ = sent[0].text
        wh_pos_ = sent[0].tag_
        wh_nbor_pos_ = sent[1].tag_
    return wh_word_, wh_pos_, wh_nbor_pos_, root_tag_