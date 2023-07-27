from django.urls import path
from .services import server_view_test, views

urlpatterns = [
    # path('', views.hello, name='hello'),

    path('sv/', server_view_test.startCrawl, name='sv_event_crawl'),  # 크롤링
    path('sv/<str:name>/', server_view_test.saveEvent, name='sv_event_save'),
    # 이벤트 리스트 페이지 응답
    path('sv/list/<str:name>/', server_view_test.showEvent, name='sv_event_list'),
    path('sv/list/<str:name>/<str:keyword>/',
         server_view_test.showEvent, name='sv_search'),

    path('<str:name>/', views.saveEvent, name='event_save'),
    # json이벤트 리스트 응답
    path('list/<str:name>/', views.showEvent, name='event_list'),
    path('list/<str:name>/<str:keyword>/', views.showEvent, name='search'),
]
