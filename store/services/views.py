from django.shortcuts import render
# from ..models import ItemGs25, ItemCu
from . import gs_crawl, cu_crawl
# from ..database.gs_repository import saveCrawlData, selectAllGS, deleteAllDatas,getGSItemsByKeyword
# import ..database.gs_repository
from ..database import cu_repository, gs_repository
from django.http import HttpResponse
import json
from django.http import JsonResponse


def hello(request):
    return render(request, 'hello/hello.html', {})

# 이벤트 크롤링 수동 버튼


def crawlEvent(request):
    # gsDatas = crawl.getScrapGSDatas()
    # print('gsDatas : ', gsDatas)
    return render(request, 'store/load-event.html', {})

# 제로필 생성


def generate_next_number(current_number):
    number = int(current_number)
    next_number = number + 1
    next_number_str = str(next_number).zfill(len(current_number))
    return next_number_str

# def hello(request):
#     return render(request, 'hello/hello.html', {})

# 이벤트 저장


def saveEvent(request, name):
    print('request :: ', request, 'name :: ', name)

    current_number = "00000"
    name = name.lower()
    context = {}

    if (request.method == 'GET'):
        if (name == 'gs25'):
            # 기존 데이터 삭제
            gs_repository.deleteAllGSDatas()
            # 새로운 크롤링 데이터 저장
            gsDatas = gs_crawl.getScrapGSDatas()
            for i in gsDatas:
                current_number = generate_next_number(current_number)
                item_idx = 'G'+current_number
                name = i['name']
                price = i['price']
                img = i['img']

                gs_repository.saveGSCrawlDatas(item_idx, name, price, img)

            context = {'items': gsDatas}

        if (name == 'cu'):
            # 기존 데이터 삭제
            cu_repository.deleteAllCUDatas()
            # 새로운 크롤링 데이터 저장
            cuDatas = cu_crawl.cu_crawl()
            for i in cuDatas:
                current_number = generate_next_number(current_number)
                item_idx = 'C'+current_number
                name = i['name']
                price = i['price']
                img = i['img']

                cu_repository.saveCUCrawlDatas(item_idx, name, price, img)

            context = {'items': cuDatas}

    return JsonResponse(context)

# 이벤트 리스트


def showEvent(request, name=None, keyword=None):
    print('request :: ', request, 'name :: ', name)

    name = name.lower()
    items = {}
    if (request.method == 'GET'):
        if (name == 'gs25'):
            if (keyword):
                items['data'] = gs_repository.searchKeyword(keyword)
            else:
                items['data'] = gs_repository.selectAllGSDatas()
        if (name == 'cu'):
            if (keyword):
                items['data'] = cu_repository.searchKeyword(keyword)
            else:
                items['data'] = cu_repository.selectAllCUDatas()

    if (len(items) > 0):
        context = {'items':  items['data'], 'name': name.upper()}
        return JsonResponse(context)

    else:
        return render(request, 'store/error.html', {'message': '리스트가 없습니다'})


# 키워드로 아이템 찾기
def searchItem(request, name, keyword):
    print('keyword : ', keyword)
    print('name : ', name)

    items = {}
    # if(name == 'gs25'):
    # items['data'] = gs_repository.getGSItemsByKeyword(keyword)

    if (len(items['data']) > 0):
        context = {'items': list(items['data']), 'name': name.upper()}

        print('==================')
        print(context)
        # 1. 화면 랜더
        return render(request, 'store/event-list.html', context)

        # 2. json응답
        # json_data = json.dumps(context)
        # return HttpResponse(json_data, content_type='application/json')
    else:
        return render(request, 'store/error.html', {'message': '리스트가 없습니다'})
