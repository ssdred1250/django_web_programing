from django.urls import path
from .views import *


urlpatterns = [
    path('', WebtoonList.as_view(), name='webtoon_list'),
    path('webtoon_naver/', Naver.as_view(), name='webtoon_naver'),
    path('webtoon_daum/', Daum.as_view(), name='webtoon_daum'),
    path('naver_webtoon/', naver_webtoon, name='naver_webtoon'),
    path('daum_webtoon/', daum_webtoon, name='daum_webtoon')
]