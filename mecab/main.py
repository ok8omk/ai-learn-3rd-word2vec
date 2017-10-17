# coding : UTF-8
import sys
import MeCab

m = MeCab.Tagger("-Ochasen")

def main():
    print("文章を入力してください (ENDを入力で終了)")
    string = input()
    while string != "END":
        print(m.parse(string))
        print("文章を入力してください (ENDを入力で終了)")
        string = input()

if __name__ == "__main__":
    main()
