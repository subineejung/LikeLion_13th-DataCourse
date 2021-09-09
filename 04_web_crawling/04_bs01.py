from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"

page = urlopen(url)  # 웹 url로부터 페이지 가져오기
print(page)

page = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
<a href="https://www.naver.com/">naver</a>
<a href="https://www.google.com">google</a>
<img height="300" src="dog_01.jpg" width="500"/>
<p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
<p> 나는 그리고 네이버 홈페이지에 자주 갑니다.</p>
<p class="p3"> 강아지 사진과 네이버 링크 </p>
<p id="p4"> 간단한 나의 홈페이지를 만들다.</p>
<p class="p3"> 강아지 사진과 네이버 링크222 </p>
</div>
</body>
</html>
'''

#
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

# 태그명 soup.태그명 => 해당되는 요소의 정보를 가져온다.
# print(soup.title)
# print(soup.body)
# print(soup.div)
# print(soup.img)
print(soup.a)
print(soup.a.text)
print(soup.div.p.text)

# id, class 을 활용해서 정보가져오기 - 하나의 요소
# id, class 을 활용해서 정보가져오기 - 모든 요소(find_all),,리스트 형태
print(soup.find("p", id="p4").text)
print(soup.find_all("p"))

# find, find_all
# naver 정보
# 모든 a태그 정보 가져오기

url = "https://naver.com"
page = urlopen(url)
print(soup.find_all("a"))
print(soup.a.text)

a1 = soup.find("a")
print(type(a1), a1.text )

a = soup.find_all("a")
print(type(a), a[1].text)

## 실습
## 한줄코드
## class 정보를 이용해서 p3인 것을 가져와서 2번째 요소의 text를 가져와보자.
p3 = soup.find("p")
print(type(p3), p3.text )

print(soup.find_all("p", class_="p3")[1].text )  # p태그이면서 p3를 가져온다, # class_

print(soup.find_all("a")[1].text )

page1 = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
</div>
<div>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역1] 필요없는 정보1 </p>
    <p class="p3"> [영역1] 필요없는 정보3 </p>
    <p id="p4"> [영역1] 필요없는 정보2 </p>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크 </p>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크222 </p>
    <p id="p4"> [영역2] 간단한 나의 홈페이지를 만들다.</p>
</div>
</body>
</html>
'''

#
soup1 = BeautifulSoup(page1, 'lxml')
print( soup1.title )

##
one_info = soup1.find_all("div")
print(len(one_info))