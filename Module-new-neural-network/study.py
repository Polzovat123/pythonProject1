from gensim.models.fasttext import FastText
from gensim.models.fasttext import FastText
from gensim.test.utils import datapath
import tempfile
import os

example = datapath("data\main.py")
print("All data open")
print(example)

model = FastText(size=300)
print("I am alive")

model.build_vocab(example)
print(model)
model.save("model.bin")
print("all complete!!!")