from wordcloud import WordCloud, STOPWORDS

import matplotlib.pyplot as plt

from konlpy.tag import Hannanum

import numpy as np

from PIL import Image

import re

text = open("contents.txt", encoding="UTF-8").read()

print(text)

myHannanum = Hannanum()

replace_text = re.sub("[!@#$%^&*()_+]", " ", text)

print(replace_text)

analysis_text = (" ".join(myHannanum.nouns(replace_text)))


stopwords = set(STOPWORDS)
# stopwords.add("전기차")
# stopwords.add("분석")
# stopwords.add("소프트웨어")

myImg = np.array(Image.open("images/doji.jpg"))

myWC = WordCloud(font_path="fonts/NGULIM.TTF", mask=myImg, stopwords=stopwords, background_color="white").generate(text)

plt.figure(figsize=(5, 5))

plt.imshow(myWC, interpolation="lanczos")

plt.axis('off')

plt.show()