from googletrans import Translator
import MeCab
import random

mecab = MeCab.Tagger("-Owakati")
translator = Translator()

select_conditions = ['助詞', '助動詞']
mecab.parse('')

#textから助詞と助動詞を除ける
def wakati_text(text):
    node = mecab.parseToNode(text)
    terms = []
    while node:
        term = node.surface
        pos = node.feature.split(',')[0]

        if not(pos in select_conditions):
            terms.append(term)

        node = node.next

    text_result = list(filter(lambda x: x != "", terms))
    return text_result

try:
    print("エセクワァトリンガル(テキスト版)") 
    print("終了したい場合はCtrl+Cを押してください")
    print("好きな文章(日本語)を入れてください")
    while True:
        text = input()
        text_tr = '' 
        text_not_tr = []
        random_num = 0
        splittedLine = mecab.parse(text).split()

        text_not = wakati_text(text)

        for i in text_not:
            random_num = random.randint(1,4)
            if random_num == 1:
                text_not_tr.append(i)
            elif random_num == 2:
                text_not_tr.append(translator.translate(i, dest='en', src='ja').text)
            elif random_num == 3:
                text_not_tr.append(translator.translate(i, dest='ko', src='ja').text)
            elif random_num == 4:
                text_not_tr.append(translator.translate(i, dest='zh-CN', src='ja').text)

        num = 0

        for i in splittedLine:
            if i in text_not:
                num += 1
                text_tr += text_not_tr[num-1]
            else:
                text_tr += i
        print(text_tr)
except KeyboardInterrupt:
    print("終了します。")
