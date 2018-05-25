from nltk.tag import StanfordNERTagger
import os

cache_file_path = "entities.json"

NER_dir = os.path.join('lib')
model_name = os.path.join(NER_dir, 'english.all.3class.distsim.crf.ser.gz')
jar_name = os.path.join(NER_dir, 'stanford-ner.jar')
st = StanfordNERTagger(model_filename=model_name, path_to_jar=jar_name)

tagged_sents = []


