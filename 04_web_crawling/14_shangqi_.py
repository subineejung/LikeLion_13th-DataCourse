from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

basic_url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=187348&target=after&page="

comment_5 = []
for i in range(1,6,1):
    real_url = basic_url + str(i)
    page = urlopen(real_url)
    soup = BeautifulSoup(page, 'html.parser')
    comment_all = soup.find_all('td', class_='title')
    print(len(comment_all))

    for one in comment_all:
        temp = list(one.children)[6].strip()
        comment_5.append(temp)

print(len(comment_5), comment_5)

dict_dat = {"댓글":comment_5}
dat = pd.DataFrame(dict_dat)
dat.to_csv("shangqi.csv", index=False)
dat.to_excel("shangqi.xlsx", index=False)