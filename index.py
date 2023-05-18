import requests 
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

from bs4 import BeautifulSoup
import time

# 페이지 이동
url = 'http://gs25.gsretail.com/gscvs/ko/products/event-goods#;'
# res = requests.get(url) 
# soup = BeautifulSoup(browser.page_source, 'html.parser')
res = browser.get(url)
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
browser.execute_script("window.scrollTo(0, 1080)") # 1920 x 1080
browser.execute_script("window.scrollTo(0, 2080)")

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
####
import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")


items = soup.find_all("div", attrs={"class":"prod_box"})
print(len(items))

for item in items:
    title = item.find("p", attrs={"class":"tit"}).get_text()
    price = item.find("span", attrs={"class":"cost"})
    img = item.find("img")['src']

    print(f"제목 : {title}")
    print(f"금액 : {price}")
    print(f"이미지 : {img}")