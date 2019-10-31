from django.urls import path
from .views import *


urlpatterns = [
    path('', WebtoonList.as_view(), name='webtoon_list'),
    path('naver_webtoon/', naver_webtoon, name='naver_webtoon'),
    path('daum_webtoon/', daum_webtoon, name='daum_webtoon')
]