from json import load
from django.http import HttpResponse
from django.template import loader
from .models import Question

# def index(request):
#     return HttpResponse("Hello World!")

# def index(request):
#     lasted_question_list = Question.objects.order_by('-pub_date')[:5]
#     # lasted_question_list 에서 루프를 돌며 넣은 q의 question_text를 배열로 만든다.
#     output = ', '.join([q.question_text for q in lasted_question_list])
#     return HttpResponse(output)

def index(request):
    lasted_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'lasted_question_list': lasted_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("detail: %s" % question_id)

def results(request, question_id):
    return HttpResponse("results: %s" % question_id)

def vote(request, question_id):
    return HttpResponse("vote: %s" % question_id)