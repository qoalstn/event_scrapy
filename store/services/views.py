from django.shortcuts import render
from ..models import ItemGs25, ItemCu
from ..services import crawl


def hello(request):
    return render(request, 'hello/hello.html', {})

# 이벤트 크롤링 수동 버튼
def crawlEvent(request):
    # gsDatas = crawl.getScrapGSDatas()
    # print('gsDatas : ', gsDatas)
    return render(request, 'store/load-event.html',{})

# 제로필 생성
def generate_next_number(current_number):
    number = int(current_number)
    next_number = number + 1
    next_number_str = str(next_number).zfill(len(current_number))
    return next_number_str


# 이벤트 저장
def saveEvent(request, name):
    print('request :: ', request)
    print('name :: ', name)

    gsDatas = crawl.getScrapGSDatas()
    current_number = "00001"

    for i in gsDatas:
        current_number = generate_next_number(current_number)
        data = ItemGs25(item_idx='G'+current_number, name=name, price=i['price'], img=i['img'])
        print('data : ',data)
        data.save()


    # if (request.method == 'POST' and name == 'gs'):
        
        # name = request.GET.get('name')
        # price = request.GET.get('price')
        # img = request.GET.get('img')

        # data = ItemGs25(item_idx='G00001', name=name, price=price, img=img)
        # data.save()
    
    # datas= [{'name' :'김부각','price' : 3000, 'img':'url1'},
    #         {'name' :'새우깡','price' : 1500, 'img':'url2'},
    #         {'name' :'스윙칩','price' : 2000, 'img':'url3'}]
    
    context = {'datas' : gsDatas}

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

