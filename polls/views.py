from json import load
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Question, Choice

# def index(request):
#     return HttpResponse("Hello World!")

# def index(request):
#     lasted_question_list = Question.objects.order_by('-pub_date')[:5]
#     # lasted_question_list 에서 루프를 돌며 넣은 q의 question_text를 배열로 만든다.
#     output = ', '.join([q.question_text for q in lasted_question_list])
#     return HttpResponse(output)

# def index(request):
#     lasted_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'lasted_question_list': lasted_question_list,
#     }
#     return HttpResponse(template.render(context, request))


def index(request):
    lasted_question_list = Question.objects.order_by("-pub_date")[:6]
    context = {
        "lasted_question_list": lasted_question_list,
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice."},
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
