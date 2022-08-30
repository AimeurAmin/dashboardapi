from django.http import HttpResponse

import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import StanfordPOSTagger
from nltk.corpus import stopwords
import spacy
import os

# WORD2VEC
import fasttext
import fasttext.util
from sklearn.linear_model import LogisticRegression

basestaticpath = '/home/amin/workspace/zahra/dashboardapi/apiapp/static'

word2vec_model = fasttext.load_model(basestaticpath +  '/StanfordPosTagger/cc.fr.128.bin')

jar = basestaticpath +  '/StanfordPosTagger/stanford-postagger.jar'
french_tagging_model = basestaticpath +  '/StanfordPosTagger/french-ud.tagger'


java_path = "/usr/lib/jvm/java-17-oracle/bin/java"
os.environ['JAVAHOME'] = java_path


nlp = spacy.load('fr_core_news_md')

# load
with open(basestaticpath +  '/model-74-precision.pkl', 'rb') as f:
    model = pickle.load(f)

# load tags
with open(basestaticpath +  '/tags_list.pkl', 'rb') as f:
    tags_dict = pickle.load(f)

def lemmatize(sentence_):
      print("LEMMA...")
      return (" ".join([token.lemma_ for token in nlp(sentence_) if (token.__len__() > 2)])).replace('n\'', 'ne')


def tokenize(sentence_):
    print("TOKENIZATION...")
    return word_tokenize(sentence_)


def pos_tagging(sentence_):
    print("POS_TAGGING...")
    pos_tagger = StanfordPOSTagger(french_tagging_model, jar, encoding='utf8')
    print(pos_tagger)
    return pos_tagger.tag(sentence_)


def remove_stopwords(sentence_):
    print("STOP_WORDS_REMOVAL...")
    french_stop_words = stopwords.words('french')
    try:
        return [(word[0], word[1]) for word in sentence_ if (word[1] != 'PUNCT' and (word[0].lower() not in french_stop_words) and word[1] != 'ADV')]
    except:
        print('something went wrong with sentence: ')
        print(sentence)
        return []


def word_to_vector(word_):
    return word2vec_model.get_word_vector(word_)


def tag_to_vector(tagg):
    return tags_dict[tagg]


def combine_word_tag(word_, tagg):
    return [*word_, *tagg]


def classifyComment(sentence):
    try:

        lemmatized = lemmatize(sentence.lower())
        print(lemmatized)

        tokenized = tokenize(lemmatized)
        print(tokenized)

        pos_tagged = pos_tagging(tokenized)
        print(pos_tagged)

        stopwords_removed = remove_stopwords(pos_tagged)
        print(stopwords_removed)

        print("RESIZING...")
        resized_sentences = (stopwords_removed * 50)[0:50:1]
        print(resized_sentences)


        print('tags_dict')
        print(tags_dict)

        combined = []
        for word_tag in resized_sentences:
            combined += combine_word_tag(word_to_vector(word_tag[0]), tag_to_vector(word_tag[1]))
            print(len(combined))

        prediction = model.predict([combined])


        print(prediction)


        switcher = {
            1: 'positif',
            0: 'neutre',
            -1: 'negatif'
        }

        prediction_as_word = switcher[prediction[0]]
        return prediction_as_word
    except:
        return 'inconnu'