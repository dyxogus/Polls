from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from polls.models import Question


def index(request):
    # Understand the Request

    # Process/Perform action of the Request
    latest_question_list = Question.objects.order_by()[:5]

    # Make appropriate response for the Request
    template = loader.get_template('polls/index.html')

    # Things we need to inflate index.html
    context = {
        'latest_question_list': latest_question_list,
    }

    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse(
        'You are looking at question %(question_id)s' % locals()
    )


def results(request, question_id):
    response = "You're looking at the results of question %(question_id)s" % locals()
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're voting on question %(question_id)s" % locals())
