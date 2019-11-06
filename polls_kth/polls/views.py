from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *


class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_data')


class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    choice = question.choice_set.get(pk=request.POST['choice'])

    choice.votes += 1
    choice.save()

    return HttpResponseRedirect('result')


class ApiQuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ApiQuestionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer




