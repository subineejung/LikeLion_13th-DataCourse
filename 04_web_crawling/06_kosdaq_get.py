# 코스닥 정보에 대한
# 지수 정보 20210908_14_index.csv
# 시황정보 뉴스 20210908_14_news.csv
# 시황정보 리포트 20210908_14_report.csv
# 인기검색어 20210908_14_pop_word.csv
# 가장 많이 본 뉴스

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

kosdaq_dat_list = ['코스닥지수', '거래량', '장중최고']
kosdaq_dat = []
# 코스닥 정보
kosdaq_info = soup.find('em', id="now_value")
print(kosdaq_info.text)

kosdaq_dat.append(kosdaq_info.text)

deal_info = soup.find('td', id='quant')
print("거래량", deal_info.text)
kosdaq_dat.append(deal_info.text)

high_info = soup.find('td', id="high_value")
print("장중최고", high_info.text)

kosdaq_dat.append(high_info.text)


# 코스닥_파일 만들기
import pandas as pd

dict_dat = { "목록":kosdaq_dat_list, "지수": kosdaq_dat  }
dat = pd.DataFrame(dict_dat)
print(dat)

dat.to_csv("kosdaq.csv", index=True)
dat.to_excel("kosdaq.xlsx", index=True)

# 시황정보
tmp_news = soup.find("ul", class_="sise_report")
tmp_li_all = tmp_news.find_all("span", class_="tit")

news= []
str1 = ""
for one in tmp_li_all:
    news.append(one.text)
print(news)

# 시황정보_파일 만들기
dat = pd.DataFrame({"코스닥 지수":news})
print(dat)
dat.to_csv("tmp_li_all.csv", index=False

# 인기검색어
hotsch = soup.find()
