from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from django.http import HttpResponseRedirect
from django.utils import timezone


class Home(ListView):
    model = Youtuber
    template_name = 'congtube/home.html'
    context_object_name = 'home_object'

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('c')

        if query:
            youtuber_list = Youtuber.objects.all(name__icontains=query)
        elif category:
            category_list = YoutuberCategory.objects.filter(category_id=category)
            youtuber_list = []

            for youtuber in category_list:
                youtuber_list.append(Youtuber.objects.get(id=youtuber.youtuber_id))
        else:
            youtuber_list = Youtuber.objects.all()

        models = {
            'youtuber_list': youtuber_list,
            'category_list': Category.objects.all()
        }
        return models


class Detail(DetailView):

    template_name = 'congtube/youtuber_detail.html'
    context_object_name = 'object'

    def get_object(self):
        youtuber_id = self.kwargs['pk']

        youtuber = Youtuber.objects.get(id=youtuber_id)
        category = YoutuberCategory.objects.filter(youtuber_id=youtuber_id)

        category_list = []
        for c in category:
            category_list.append(Category.objects.get(id=c.category_id))

        subscriber_count = len(Subscriber.objects.filter(youtuber_id=youtuber_id))

        youtuber.view += 1
        youtuber.save()

        models = {
            'youtuber': youtuber,
            'category': category_list,
            'review': Review.objects.filter(youtuber_id=youtuber_id),
            'recommend': Youtuber.objects.filter(~Q(id=youtuber_id)),
            'subscriber_count': subscriber_count
        }

        return models


def add_review(request, pk):
    review = Review()
    review.youtuber_id = pk
    review.user_id = 1
    review.review_text = request.POST['review']
    review.register_date = timezone.now()

    review.save()

    return HttpResponseRedirect('/')


def add_subscriber(request, pk):
    subscriber = Subscriber()
    subscriber.youtuber_id = pk
    subscriber.user_id = 1
    subscriber.register_date = timezone.now()

    subscriber.save()

    return HttpResponseRedirect('/detail/' + str(pk))