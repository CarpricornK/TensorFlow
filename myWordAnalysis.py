from konlpy.tag import Hannanum

import re

myHannanum = Hannanum()

myHannanum.analyze
myHannanum.morphs
myHannanum.nouns
myHannanum.pos

text = "전기차 품귀 현상 속에 일부 인기 모델이 내년 말까지 계획한 출고 계약을 모두 마감했다."\
"신규 계약을 일시 중단하는 대리점도 나타났다. "\
"구매 희망자가 크게 늘어났지만 부품난 등으로 증산이 어려워지면서 공급과 수요 불균형이 심화된 영향이다."\
"31일 국내에 시판 중인 전기차가 가운데 소비자 선호도가 높은 인기 모델의 계약 후 출고까지 대기 기간이 1년을 상회하는 것으로 나타났다."\
"현대차 주력 전기차 아이오닉5는 1년, 지난 7월에 나온 신차 아이오닉6는 1년 6개월이 걸린다."

replace_text = re.sub("[!@#$%^&*()_+]", " ", text)

print(replace_text)

print(myHannanum.nouns(replace_text))

# print(myHannanum.analyze(text))