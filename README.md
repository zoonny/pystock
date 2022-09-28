# pystock

## Django 설치 및 설정
```shell
$ pip install Django=4.1.1
$ django-admin startproject pystock

# git pull = git fetch + git merge
$ fatal: refusing to merge unrelated histories
$ git pull origin main --allow-unrelated-histories

$ cd pystock
$ python manage.py runserve
$ python manage.py runserve 8080
$ python manage.py runserve 0:8080

$ django-admin startapp polls
$ django-admin startapp stock

# settings.py
$ ...

$ python manage.py migrate

$ python manage.py makemigrations polls
Migrations for 'polls':
  polls\migrations\0001_initial.py
      - Create model Question
          - Create model Choice
$ python manage.py sqlmigrate polls 0001
$ python manage.py migrate
$ python manage.py migrate polls
```

- Django Data Handling

```shell
$ python manage.py shell
```

```python
from polls.models import Choice, Question
Question.objects.all()
from django.utils import timezone
q = Question(question_text="What's news?", pub_date=timezone.now())
q.save()
q.id
q.question_text
q.pub_date
q.question_text = 'Hi there?'
q.save()
Question.objects.all()
```

```python
from polls.models import Choice, Question
Question.objects.all()
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')
from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
# returned more than one Question -- it returned 3!
# should only one element return
Question.objects.get(id=2)
q = Question.objects.get(pk=1)
q.was_published_recently()
# display child entity (foregin key) - empty set
q.choice_set.all()
# <QuerySet []>
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
q.choice_set.create(choice_text='HaHa', votes=0)
c = q.choice_set.create(choice_text='hoho', votes=0)
# display super entity
c.question
q.choice_set.all()
q.choice_set.count()
Choice.objects.filter(question__pub_date__year=current_year)
c = q.choice_set.filter(choice_text__startswith='ho')
c.delete()
q.choice_set.all()
```

- 수정파일
    - pystock/settings.py
    - pystock/urls.py

- python formatter
```shell
$ pip install black

# setting balck on formatting provider in vscode

```

## Django admin

```shell
# 관리자 사용자 생성
$ python3 manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: ******
$ python manage.py runserver
```
> http://localhost:8000/admin

- manage poll app in admin site
    - code to polls/admin.py
```python
from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
```

