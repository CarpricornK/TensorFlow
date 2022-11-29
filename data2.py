import pickle
import tensorflow as tf
import re
from konlpy.tag import Okt
from tensorflow.python import keras
from keras.preprocessing.sequence import pad_sequences

loaded_model = tf.keras.model.load.model("model/naver_movie.h5")

stopwords = ['의','가','이','은','들','는','좀','잘','강','과','도','를','으로','자','에','와','한','하다']

with open("model/tokenizer.pickle", "rb") as handle:
   tokenizer = pickle.load(handle)


okt = Okt()

max_len = 30

def sentiment_predict(new_sentence) :
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣]','', new_sentence)
    new_sentence = okt.morphs(new_sentence, stem=True)
    new_sentence = [word for word in new_sentence if not word in stopwords]
    encoded = tokenizer.texts_to_sequences([new_sentence])
    pad_new = pad_sequences(encoded, maxlen = max_len)

    score = float(loaded_model.predict(pad_new))
    if(score > 0.5):
        print("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(score * 100))
    else:
        print("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 -score) * 100))

sentiment_predict('이 영화 재미 없다.')

sentiment_predict('배우 연기가 별로다')

sentiment_predict('망한 영화인가?')


