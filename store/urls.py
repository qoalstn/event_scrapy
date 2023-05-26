from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('list/', views.showEvent, name='event_list'),
    path('regist/gs', views.saveEventGS, name='event_regist_gs'),
    path('regist/cu', views.saveEventCU, name='event_regist_cu'),
]
