# -*- coding: utf8 -*-
from mango_connector import connect_and_push_to_dataset_data
from gensim.models import Word2Vec
import gensim.downloader
import fasttext
from gensim.models.fasttext import FastText
import numpy as np
from scipy import spatial
import math
SIZE = 2
have = True

def use_mango_connector(title, link, link_web_site, id, image='not found'):
    l_title = convert_dict_to_list(title)
    connect_and_push_to_dataset_data(title, id, link, link_web_site, image, get_array_thems(l_title))

'''    print(title)
    print(link)
    print(get_array_thems(title))'''
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

def convert_dict_to_list(dictt):
    l = []
    for i in range(len(dictt)):
        l.append(dictt[i]['title'])
    return l

def init_atr():
    return ['политика', 'экономика', 'общество', 'история', 'медицина', 'технологии']

def get_array_thems(title):
    ans = []
    path = 'Module-new-neural-network/aii/model.bin'
    model = FastText.load(path)
    for i in range(len(title)):
        ans.append(get_one_header_news_element(title[i], model))
    return ans

def get_one_header_news_element(words, model):
    ans = []
    atribute = init_atr()
    wordi = clear_words(words)
    for cat in atribute:
        ans.append(difference(cat, wordi, model))
    return choice_better(ans)

def clear_words(sen):
    sen = sen.lower()
    index = 0
    for i in sen:
        if (i>='а' and i<='я')==False:
            sen = sen[:index] + sen[index:]
        if (i >= 'а' and i <= 'я') == False and index==len(sen)-1:
            sen = sen[:index]
        index+=1
    print(sen)
    print(type(sen))
    return sen.split()

def difference(first_word, words, model):
    res = 0
    for i in range(len(words)):
        res += model.similarity(first_word, words[i])
    return res

def check_have_ans(v, z):
    for i in v:
        if i==z:
            return False
    return True

def choice_better(vec):
    a = []
    bb = 0
    for i in range(SIZE):
        best = 0
        for cat in range(len(vec)):
            if best < vec[cat] and check_have_ans(a, cat):
                best = vec[cat]
                bb = cat
        a.append(bb)
    return a

'''
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
    return " "'''