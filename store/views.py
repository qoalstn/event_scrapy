from django.shortcuts import render
from .models import ItemGs25, ItemCu


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.maximize_window()
from bs4 import BeautifulSoup
import re
import time


def hello(request):
    return render(request, 'hello/hello.html', {})

# 이벤트 크롤링 수동 버튼
def crawlEvent(request):
    return render(request, 'store/load-event.html',{})


# 이벤트 저장
def saveEvent(request, name):
    print('request :: ', request)
    print('name :: ', name)

    if (request.method == 'POST' and name == 'gs'):
        scrapGSDatas()
        # name = request.GET.get('name')
        # price = request.GET.get('price')
        # img = request.GET.get('img')

        # data = ItemGs25(item_idx='G00001', name=name, price=price, img=img)
        # data.save()
    
    datas= [{'name' :'김부각','price' : 3000, 'img':'url1'},
            {'name' :'새우깡','price' : 1500, 'img':'url2'},
            {'name' :'스윙칩','price' : 2000, 'img':'url3'}]
    
    context = {'datas' : datas}

    return render(request, 'store/event.html',context)

# 이벤트 리스트
def showEvent(request, name):
    print('request :: ', request)
    print('storeName : ', name)

    items = []
    if (request.method == 'GET'):
        if (name == 'gs'):
            items.append(getItemsByStore(ItemGs25))
        if (name == 'cu'):
            items.append(getItemsByStore(ItemCu))

    print('items : ', items)

    return render(request, 'store/event-list.html')

# 편의점 별 아이템 리스트 가져오기
def getItemsByStore(model):
    return model.objects.all()

def scrapGSDatas():
    print('통과')
    # 페이지 이동
    url = 'http://gs25.gsretail.com/gscvs/ko/products/event-goods#;'
    res = browser.get(url)
    page_soup = BeautifulSoup(browser.page_source, 'html.parser')


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
    # time.sleep(2)
    # print('text : ', page_soup.select('a.next2')[0])
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
        items = page_soup.find_all("div", attrs={"class":"prod_box"})

        print('prod_box len : ', len(items))
        
        for item in items:
            title = item.find("p", attrs={"class":"tit"}).get_text()
            price = item.find("span", attrs={"class":"cost"})
            img = item.find("img")['src']

            # print(f"제목 : {title}")
            # print(f"금액 : {price}")
            # print(f"이미지 : {img}")

        next_page = browser.find_element(By.XPATH,'//*[@id="contents"]/div[2]/div[3]/div/div/div[1]/div/a[3]')
        next_page.click()