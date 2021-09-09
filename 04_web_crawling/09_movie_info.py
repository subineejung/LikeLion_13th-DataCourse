from bs4 import BeautifulSoup
from urllib.request import urlopen

# 웹 페이지 소스 가져오기 및 파싱
url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')

print(soup.title)

### 상영작/예정작 제목만 뽑기
soup_ul_li = soup.find("ul", class_='lst_detail_t1').find_all("li")
print(len(soup_ul_li))

print(soup_ul_li[3].find("dt", class_="tit").a.text)

### 평점
print(soup_ul_li[0].find("span", class_="num").text)

### 참여 명수
print(soup_ul_li[0].find("em").text)



print(soup_ul_li[0].find("dl", class_="info_exp").span.text)

### 개요
txt = soup_ul_li[0].find("span", class_="link_txt").text
txt_last = txt.replace("\n", "")
txt_last = txt_last.replace("\t", "")
txt_last = txt_last.replace("\r", "")
# print(soup_ul_li[0].find("span", class_="link_txt").text)
print(txt_last)

#  제목, 평점, 참여수, 개요
all_title = []
all_score = []
all_people = []
all_category = []
all_rate = []


for one in soup_ul_li:
    title = one.find("dt", class_="tit").a.text
    score = one.find("span", class_="num").text
    people = one.find("em").text
    tmp = one.find("dl", class_="info_exp")


    ### 예매율
    tmp = one.find("dl", class_="info_exp")
    if tmp is not None:
        rate = tmp.span.text
    else:
        rate = 0

    category = one.find("span", class_="link_txt").text
    txt_last = category.replace("\n", "")
    txt_last = txt_last.replace("\t", "")
    txt_last = txt_last.replace("\r", "")

    all_title.append(title)
    all_score.append(score)
    all_people.append(people)
    all_rate.append(rate)
    all_category.append(txt_last)

print(len(all_title), len(all_score), len(all_people), len(all_category), len(all_rate))

## 저장을 위한 csv, xlsx파일 만들기

import pandas as pd

dat_dict = {
    "제목":all_title, "평점":all_score, "참여명수":all_people, "예매율":all_rate, "개요":all_category }
dat = pd.DataFrame(dat_dict)
dat.to_csv("네이버영화.csv", index=False)
dat.to_excel("네이버영화.xlsx", index=False)

