from sklearn.feature_extraction.text import CountVectorizer
from konlpy.tag import Okt
import re
okt=Okt()

token=re.sub("(\.)","","한국폴리텍대학 서울강서캠퍼스 데이터분석과 이협건 교수는"
             "한국폴리텍대학에서 데이터분석 과목과 인공지능 과목을 교육하는 교수이다.")

token=okt.morphs(token)

corpus = [" ".join(token)]

vector = CountVectorizer()

print(vector.fit_transform(corpus).toarray())

print(vector.vocabulary_)

word2index={}
bow=[]

for word in token:

    if word not in word2index.keys():

        word2index[word]=len(word2index)

        bow.insert(len(word2index)-1,1)

    else:

        index=word2index.get(word)

        bow[index]=bow[index]+1

#
# print(word2index)
#
# print(bow)