# coding : utf-8
from gensim.models import word2vec
import sys

while True:
    print("単語を入力してください")
    print("(Ctrl-cで終了)")
    word = input()
    for i in range(25, 101, 25):
        input_file = 'models/yume_juya_{}.model'.format(i)
        model = word2vec.Word2Vec.load(input_file)
        results = model.most_similar(word)
        print('[{}]vector : {}-dim'.format(word, i))
        print('|順位|名前|類似度|')
        for i, (key, val) in enumerate(results):
            print('|{}|{}|{}|'.format(i+1, key, val))
