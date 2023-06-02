from django.shortcuts import render
from .models import ItemGs25, ItemCu


def hello(request):
    return render(request, 'hello/hello.html', {})

# 이벤트 크롤링 수동 버튼
def crawlEvent(request):
    return render(request, 'store/load-event.html',{})


# 이벤트 저장
def saveEvent(request, name):
    print('request :: ', request)

    if (request.method == 'POST'):
        name = request.GET.get('name')
        price = request.GET.get('price')
        img = request.GET.get('img')

        data = ItemGs25(item_idx='G00001', name=name, price=price, img=img)
        data.save()
    
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
