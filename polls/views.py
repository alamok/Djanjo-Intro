from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from elasticsearch import Elasticsearch as ES

from .models import Question


def index(request):
    # test a elastic search connection and create index 
    # if index already exists dont do anything

    es = ES('http://127.0.0.1:9200/')
    es.indices.create(index='test-rule1', ignore=400)
    # we may need to create a function here to hold another template in case elastic search
    # does not load.

    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
        })
    #output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse("you are looking at the results of question %s" % question_id)

def results(request, question_id):
    response = "you are looking at the results of question %s"
    return HttpResponse(response % question_id )

def vote(request, question_id):
    return HttpResponse("you are voting for the question %s." % question_id)

def test( request ):
    template = loader.get_template('polls/test.html')
    response = "this is a test"
    #return HttpResponse( response )
    return HttpResponse(template.render())
