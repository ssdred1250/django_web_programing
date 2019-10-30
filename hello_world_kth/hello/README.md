 ### 1. 장고 설치
 ```pip install django```
 ### 2. 프로젝트 설치
 ```django-admin startproject config .```
 ### 3. 데이터베이스 생성 및 적용
 ```python manage.py migrate```
 ### 4. 개발 서버 실행
 ```python manage.py runserver```
 ### 5. 관리자 계정 생성
 ```python manage.py createsuperuser```
 ### 6. 앱 설치
 ```python manage.py startapp hello```
 
 ### hello/views.py
 컨트롤러
 ```
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!")
```

### hello/urls.py
```
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world')
]
```

### config/urls.py
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', include('hello.urls'))
]
```

### 순서
/hello_world/ - url \
config/urls.py \
hello/urls.py \
hello/views.py


