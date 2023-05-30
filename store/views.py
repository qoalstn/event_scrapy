from django.shortcuts import render
from .models import ItemGs25, ItemCu


def hello(request):
    return render(request, 'hello/hello.html', {})


def saveEvent(request):
    print('request :: ', request)

    if (request.method == 'GET'):
        name = request.GET.get('name')
        price = request.GET.get('price')
        img = request.GET.get('img')

        data = ItemGs25(item_idx='G00001', name=name, price=price, img=img)
        data.save()

    return render(request, 'store/event.html')


def showEvent(request, name):
    print('request :: ', request)
    print('storeName : ', name)

    items = []
    if (request.method == 'GET'):
        if (name == 'gs'):
            items.append(getItems(ItemGs25))
        if (name == 'cu'):
            items.append(getItems(ItemCu))

    print('items : ', items)

    return render(request, 'store/event-list.html')


def getItems(model):
    return model.objects.all()
