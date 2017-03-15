from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by()[:5]

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse(
        'You are looking at question %(question_id)s' % locals()
    )


def results(request, question_id):
    response = "You're looking at the results of question %(question_id)s" % locals()
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're voting on question %(question_id)s" % locals())
