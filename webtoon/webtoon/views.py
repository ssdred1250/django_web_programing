from django.shortcuts import render
import webtoon.daum_webtoon
import webtoon.naver_webtoon

from django.http import HttpResponse
from django.views.generic import ListView
from .models import Webtoon


def naver_webtoon(request):
    webtoon.naver_webtoon.webtoon_all()
    return HttpResponse('네이버 웹툰 크롤링 완료')


def daum_webtoon(request):
    webtoon.daum_webtoon.webtoon_all()
    return HttpResponse('다음 웹툰 크롤링 완료')


class WebtoonList(ListView):
    model = Webtoon
    paginate_by = 40


class Naver(ListView):
    queryset = Webtoon.objects.filter(site_name='naver')
    paginate_by = 40


class Daum(ListView):
    queryset = Webtoon.objects.filter(site_name='daum')
    paginate_by = 40




