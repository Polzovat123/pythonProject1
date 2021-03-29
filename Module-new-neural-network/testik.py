# -*- coding: utf8 -*-
from gensim.models.fasttext import FastText
import numpy as np
import math

politic = []
economic =[]
society = []
spiritual = []
def init_atr():
    return ['политика', 'экономика', 'общество', 'история']

def get_array_thems(title):
    ans = []
    path = 'aii/model.bin'
    model = FastText.load(path)
    for i in range(len(title)):
        ans.append(get_one_header_news_element(title[i], model))
    return ans

def get_one_header_news_element(words, model):
    ans = []
    theme = np.zeros(300)
    sentence = words.lower().split()
    atribute = init_atr()
    for cat in atribute:
        ans.append(difference(cat, words, model))
    return ans

def difference(first_word, words, model):
    res = 0
    for i in range(len(words)):
        res += model.similarity(first_word, words[i])
    return res



title = ['"Эвер Гивен" в Суэцком канале: владельцы надеются снять судно с мели, но на это могут уйти недели', 'Коронавирус после прививки: как сильно люди болеют и почему это происходит?']
print(get_array_thems(title))