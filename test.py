from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn

dog_sets = wn.synsets('people')
for set in dog_sets:
    print(set)

print()

print(dog_sets[0].hypernym_paths())

print(dog_sets[0].topic_domains())
print(dog_sets[0].usage_domains())

print(dog_sets[0].lemmas()[0].key())
