import requests 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.maximize_window()

from bs4 import BeautifulSoup

import re
import time

def getScrapGSDatas():
    datas = []
    # 페이지 이동
    url = 'http://gs25.gsretail.com/gscvs/ko/products/event-goods#;'
    res = browser.get(url)


    ## 스크롤
    # 현재 문서 높이를 가져와서 저장
    prev_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # 스크롤을 가장 아래로 내림
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # 페이지 로딩 대기
        time.sleep(2)

        # 현재 문서 높이를 가져와서 저장
        curr_height = browser.execute_script("return document.body.scrollHeight")
        if curr_height == prev_height:
            break

        prev_height = curr_height

    print("스크롤 완료")

    page_soup = BeautifulSoup(browser.page_source, 'html.parser')
    p = re.compile('(?<=movePage\()(.*?)(?=\))')
    text =page_soup.select('a.next2')[0]
    rs = p.findall(str(text))

    last_page = int(rs[0])
    print(last_page)

    for i in range(1, 3) :
        while True:
            # 스크롤을 가장 아래로 내림
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            # 페이지 로딩 대기
            time.sleep(2)

            # 현재 문서 높이를 가져와서 저장
            curr_height = browser.execute_script("return document.body.scrollHeight")
            if curr_height == prev_height:
                break

            prev_height = curr_height

            print("스크롤 완료")
        page_soup = BeautifulSoup(browser.page_source, 'html.parser')
        # items = page_soup.find_all("div", attrs={"class":"prod_box"})
        list = page_soup.find("ul", {"class":"prod_list"})
        if list:
            items = list.find_all("div", {"class":"prod_box"})
        else :
            print('list가 없습니다')

        print('prod_box len : ', len(items))
        
        for item in items:
            title = item.find("p", attrs={"class":"tit"}).get_text()
            price_str = item.find("span", attrs={"class":"cost"}).get_text()
            price = re.sub(r"[^\d]+","",price_str)
            img = item.find("img")['src']

            print(f"page :  {i},제목 : {title}")
            print(f"page :  {i},금액 : {price}")
            print(f"page :  {i},이미지 : {img}")

            datas.append({'title' : title, 'price' : price, 'img':img})

        next_page = browser.find_element(By.XPATH,'//*[@id="contents"]/div[2]/div[3]/div/div/div[1]/div/a[3]')
        next_page.click()

    return datas