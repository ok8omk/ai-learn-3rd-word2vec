# coding : UTF-8
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format( \
        "./entity_vector/entity_vector.model.bin", binary=True)

def similar():
    while True:
        print("単語を入力してください\n \
                ( Ctrl-cで終了)")
        word = input()
        sims = model.most_similar(word)
        print("|順位|名前|類似度|")
        for i, (key, val) in enumerate(sims):
            print("|{}|{}|{}|".format(i+1, key, val))

def calculate():
    while True:
        print("演算したい単語をスペースを開けて入力してください\n \
                ( Ctrl-cで終了 ) \n \
                例: 札幌市 - 北海道 = ??? - 沖縄県の場合 \n \
                    入力 -> 札幌市 北海道 沖縄県")
        words = input().split()
        words = [ '[' + word + ']' for word in words ]
        if len(words) != 3:
            print("正しく3つの単語を入力してください")
        else:
            sims = model.most_similar( \
                    positive=[words[0], words[2]], \
                    negative=[words[1]])
            print("|順位|名前|類似度|")
            for i, (key, val) in enumerate(sims):
                print("|{}|{}|{}|".format(i+1, key, val))

if __name__ == "__main__":
    similar()
    #calculate()
