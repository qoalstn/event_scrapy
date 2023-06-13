import json
import re
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


headers = {
    "Referer": "https://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N",
    "User-Agent": "2/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

}

def cu_crawl():
    sale_product = []
    for i in range(1, 2):
        params = {
            "pageIndex": i,
            "listType": 1,
            "searchCondition": "",
            "user_id": ""
        }
    res = requests.post(
        "https://cu.bgfretail.com/event/plusAjax.do", headers=headers, data=params)
    soup = BeautifulSoup(res.text, "html.parser")
    prod_badge = soup.find_all('div', "badge")
    for b in prod_badge:
        badges = b.find_all(["span"])
        for badge in badges:
            sale_badge = badge.text
    prod_all = soup.find_all("div", {'class': 'prod_wrap'})
    for i in prod_all:
        prod_name = i.find_all(['p'])
        for name in prod_name:
            sale_name = name.text
        prod_price = i.find_all(['strong'])
        for price in prod_price:
            sale_price = price.text+"원"
        prod_img = i.find_all("img")

        for img in prod_img:
            img_src = "http" not in img['src']
            if img_src:
                sale_src = "https:"+img['src']
            else:
                sale_src = img['src']
        sale_product.append({'name': sale_name, 'price': sale_price,
                        'img': sale_src, 'plus': sale_badge})
        
        # print(json.dumps(sale_product, ensure_ascii=False, indent=2))
    print(sale_product)   
    
    return sale_product   
