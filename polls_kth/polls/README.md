 ## 1. 프로젝트 준비
 ### 1. 장고 설치
 ```
 $ pip install django
```
 ### 2. 프로젝트 설치
 ```
 $ django-admin startproject config .
```
 
 ### 3. 데이터베이스 생성 및 적용
 ```
 $ python manage.py migrate
```

 ### 4. 개발 서버 실행
 ```
 $ python manage.py runserver
```

 ### 5. 관리자 계정 생성
 ```
 $ python manage.py createsuperuser
```
127.0.0.1:8000/admin 으로 접속 가능
 ### 6. polls 앱 설치
 ```
 $ python manage.py startapp polls
```
 polls 폴더 생성\
 config/settings.py 에서 polls 앱을 등록
 ```buildoutcfg
INSTALLED_APPS = [
...
    'polls',
...
]
```
config/urls.py 에서 polls 앱 url 등록
```buildoutcfg
from django.urls import path, include

urlpatterns = [
...
    path('polls/', include('polls.urls'))
...
]
```
 webtoon/urls.py 생성
 ## 2. index 페이지 만들기
 ### 2-1. model 작성
 - polls/models.py
 ```
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choice', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```
- migration 파일 생성
```
$ python manage.py makemigrations
```
- DB에 반영
```
$ python manage.py migrate
```

 ### 2-2. view class 작성
- polls/view.py
 ```
from django.views import generic
from .models import *

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_data')
```

### 2-3. template 작성
- polls/templates/index.html - body
```
{% if latest_question_list %}
    <ul>
        {% for question in latest_question_list %}
            <li>
                <a href="/polls/{{ question.id }}">{{ question.question_text }}</a>
            </li>
        {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

### 2-4. url 등록
- polls/urls.py 
```
from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
```
### 2-5. admin 페이지에서 vote 생성
- polls/admin.py
```
from django.contrib import admin
from .models import *


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
```
127.0.0.1:8000/admin 에서 투표 생성

## 3. detail 페이지 만들기
### 3-1. view class 작성
```
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
```





 
 