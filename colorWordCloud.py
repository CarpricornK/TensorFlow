# Numpy는 다차원 배열을 쉽게 처리하고 효율적으로 사용할 수 있도록지원하는 파이썬의
# 패키지입니다. NumPy는 데이터 구조 외에도 수치 계산을 위해 효율적으로 구현된
# 기능을 제공합니다 ※강조numpy뭔지 꼭알자※
import numpy as np

from PIL import Image

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

from konlpy.tag import Hannanum

import re

text = open("contents.txt", encoding="UTF-8").read()

myHannanum = Hannanum()

replace_text = re.sub("[!@#$%^&*()_+]", " ", text)

print(replace_text)

analysis_text = (" ".join(myHannanum.nouns(replace_text)))

stopwords = set(STOPWORDS)
# stopwords.add("전기차")
# stopwords.add("분석")
# stopwords.add("소프트웨어")

myImg = np.array(Image.open("images/doji.jpg"))

imgColor = ImageColorGenerator(myImg)

myWC = WordCloud(font_path="fonts/NGULIM.TTF", mask=myImg, stopwords=stopwords, background_color="white").generate(text)

plt.figure(figsize=(5, 5))

plt.imshow(myWC.recolor(color_func=imgColor), interpolation="lanczos")

plt.axis('off')

plt.show()