from django.urls import path
from .services import server_view_test, views

urlpatterns = [
    # path('', views.hello, name='hello'),

    # ============================================================================
    # 서버테스트용
    # ============================================================================
    # 시작페이지
    path('sv/', server_view_test.startCrawl, name='sv_event_crawl'),
    # 크롤링 및 저장
    path('sv/<str:name>/', server_view_test.saveEvent, name='sv_event_save'),
    # 리스트
    path('sv/list/<str:name>/', server_view_test.showEvent, name='sv_event_list'),
    # 검색
    path('sv/list/<str:name>/<str:keyword>/',
         server_view_test.showEvent, name='sv_search'),

    # ============================================================================
    # 클라이언트 응답
    # ============================================================================
    # 크롤링 및 저장
    path('<str:name>/', views.saveEvent, name='event_save'),
    # 리스트
    path('list/<str:name>/', views.showEvent, name='event_list'),
    # 검색
    path('list/<str:name>/<str:keyword>/', views.showEvent, name='search'),
]
