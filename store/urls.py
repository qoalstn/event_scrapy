from django.urls import path
from .services import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('crawl/', views.crawlEvent, name='event_crawl'),
    path('<str:name>/',
         views.saveEvent, name='event_save'),
    path('list/<str:name>/',
         views.showEvent, name='event_list'),
    #     path('search/<str:keyword>/',
    #          views.searchItem, name='search'),
]
