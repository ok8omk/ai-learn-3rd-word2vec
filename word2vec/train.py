from gensim.models import word2vec
import logging
import sys

input_path  = 'resources/yume_juya_wakati.txt'

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

for i in range(25, 101, 25):
    size = i
    output_path = 'models/yume_juya_' + str(i) + '.model'
    sentences = word2vec.LineSentence(input_path)
    model = word2vec.Word2Vec(sentences,
            sg=1,
            size=i,
            min_count=1,
            window=10,
            hs=1,
            negative=0,
            iter=50
    )
    model.save(output_path)
