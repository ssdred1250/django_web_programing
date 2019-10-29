from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('투표 목록입니다.')


def detail(request, question_id):
    return HttpResponse(str(question_id) + '번째 투표 상세 화면입니다.')


def result(request, question_id):
    return HttpResponse(str(question_id) + '번째 투표 결과 화면입니다.')
