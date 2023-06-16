from django.urls import path
from .services import server_view_test, views

urlpatterns = [
    # path('', views.hello, name='hello'),

    path('sv/', server_view_test.startCrawl, name='sv_event_crawl'),
    path('sv/<str:name>/', server_view_test.saveEvent, name='sv_event_save'),
    path('sv/list/<str:name>/', server_view_test.showEvent, name='sv_event_list'),
    path('sv/list/<str:name>/<str:keyword>/',server_view_test.showEvent, name='sv_search'),

    path('<str:name>/', views.saveEvent, name='event_save'),
    path('list/<str:name>/', views.showEvent, name='event_list'),
    path('list/<str:name>/<str:keyword>/',views.showEvent, name='search'),
]
