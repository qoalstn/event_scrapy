from django.shortcuts import render
from .models import ItemGs25


def hello(request):
    return render(request, 'hello/hello.html', {})


def saveEvent(request):
    print('request :: ', request)

    # template_values = { 
    #     'name' : '방울토마토',
    #     'price' : 2000,
    #     'img' : 'https://image.woodongs.com/imgsvr/item/GD_8809168367350_001.jpg'
    # } 
    return render(request, 'store/event.html')

def showEventGS(request):
    print('request >>',request.GET.get('name'))

    if(request.method == 'GET'):
        name = request.GET.get('name')
        price = request.GET.get('price')
        img = request.GET.get('img')

        data = ItemGs25(item_idx='G00001',name=name, price=price, img=img)
        data.save()

        new_data = ItemGs25.objects.all()

        print('new_data >> ', new_data)


        # data = ItemGs25(template_values)
        # data.save()
    return render(request, 'store/event.html')

def showEventCU(request):
    print('request >>',request.GET.get('name'))

    if(request.method == 'GET'):
        name = request.GET.get('name')
        price = request.GET.get('price')
        img = request.GET.get('img')

        data = ItemGs25(item_idx='G00001',name=name, price=price, img=img)
        data.save()

        new_data = ItemGs25.objects.all()

        print('new_data >> ', new_data)


        # data = ItemGs25(template_values)
        # data.save()
    return render(request, 'store/event.html')
