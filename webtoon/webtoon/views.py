from django.shortcuts import render
from .naver_webtoon import webtoon_all
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Webtoon


def naver_webtoon(request):
    webtoon_all()
    return HttpResponse('네이버 웹툰 크롤링 완료')


class WebtoonList(ListView):
    model = Webtoon


