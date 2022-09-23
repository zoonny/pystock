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

```shell
$ python manage.py shell
```

```python
from polls models import Choice, Question
Question.objects.all()
from django.utils import timezone
q = Question(question_text="What's news?", pub_date=timezone.now())
q.save()
q.id
q.question_text
q.pub_date
```

- 수정파일
    - pystock/settings.py
    - pystock/urls.py

- python formatter
```shell
$ pip install black

# setting balck on formatting provider in vscode

```
