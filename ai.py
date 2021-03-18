from mango_connector import connect_and_push_to_dataset_data
from gensim.models import Word2Vec
import gensim.downloader
from gensim.models import FastText
import numpy as np
from scipy import spatial

have = True

def use_mango_connector(title, link, link_web_site, id, image='not found'):
    connect_and_push_to_dataset_data(title, id, link, link_web_site, image, get_dict_thems(title))
'''
ans = {
    'politic':0,
    'economic':0,
    'society':0,
    'spiritual':0
}
'''
politic = []
economic =[]
society = []
spiritual = []


def get_dict_thems(title):
    ans = []
    for i in range(len(title)):
        analysis_text(title[i]['title'])

    return ans

def analysis_text(word):
    global have
    if have:
        model = Word2Vec.load("word2vec.model")
    else:
        model = life_vector()
        model.save("word2vec.model")
        have = True
        print(word)
    return difference(word, model)


def life_vector():
    return gensim.downloader.load('glove-wiki-gigaword-300')

def difference(s, model):
    word = model[get_main_word(s)]
    vec = {
        'politic': difference_between_two_words(politic, word),
        'economic': difference_between_two_words(economic, word),
        'society': difference_between_two_words(society, word),
        'spiritual': difference_between_two_words(spiritual, word)
    }
    return vec

def difference_between_two_words(first, second):
    return 0

def get_main_word(s):
    return " "