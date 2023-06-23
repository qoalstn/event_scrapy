from django.shortcuts import render
from . import gs_crawl, cu_crawl
from ..database import gs_repository, cu_repository
from .util import generate_next_number

# 이벤트 크롤링 수동 버튼 // TODO : 매월초 자동 스케쥴링
def startCrawl(request):
    return render(request, 'store/load-event.html',{})

# 이벤트 저장
def saveEvent(request, name):
    print('request :: ', request, 'name :: ', name)

    name = name.lower()
    current_number = "00000" 

    if (request.method == 'GET'):
        if (name == 'gs25'):
            # 기존 데이터 삭제
            gs_repository.deleteAllGSDatas()
            # 새로운 크롤링 데이터 저장
            gsDatas = gs_crawl.getScrapGSDatas()
            for i in gsDatas:
                current_number = generate_next_number(current_number)
                item_idx = 'G'+current_number
                title = i['title']
                price = i['price']
                img = i['img']
                
                gs_repository.saveGSCrawlDatas(item_idx,title,price,img)
            
            context = {'items' : gsDatas}

        if (name == 'cu'):
            # 기존 데이터 삭제
            cu_repository.deleteAllCUDatas()
            # 새로운 크롤링 데이터 저장
            cuDatas = cu_crawl.cu_crawl()
            for i in cuDatas:
                current_number = generate_next_number(current_number)
                item_idx = 'C'+current_number
                title = i['title']
                price = i['price']
                img = i['img']
                
            cu_repository.saveCUCrawlDatas(cuDatas)
            
            context = {'items' : cuDatas}

    return render(request, 'store/event-list.html',context)

# 이벤트 리스트
def showEvent(request, name=None, keyword=None):
    print('request :: ', request, 'name :: ', name)

    name = name.lower()
    items = {}
    if (request.method == 'GET'):
        if (name == 'gs25'):
            if(keyword):
                items['data'] = gs_repository.searchKeyword(keyword)
            else:
                items['data'] = gs_repository.selectAllGSDatas()
        if (name == 'cu'):
            if(keyword):
                items['data'] = cu_repository.searchKeyword(keyword)
            else:
                items['data'] = cu_repository.selectAllCUDatas()

    # print('items : ',  items['data'] )

    if(len(items) > 0):
        context = {'items' :  items['data'] , 'name':name.upper()}
        
        return render(request, 'store/event-list.html',context)
    
    else:
        return render(request, 'store/error.html',{'message':'리스트가 없습니다'})




