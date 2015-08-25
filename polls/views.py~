from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from elasticsearch import Elasticsearch as ES
from django import forms
#This is how get get rid of bloody csrf after you could't properly
#fix it after 1 hour of googleing... jesus
from django.views.decorators.csrf import csrf_exempt

from .models import Question
import sys

class QuestionInfo:
    def __init__( self, id, text ):
        self.questionId = id
        self.questionText = text;

def index(request):
    # test a elastic search connection and create index 
    # if index already exists dont do anything

    es = ES('http://127.0.0.1:9200/')
    es.indices.create(index='test-rule1', ignore=400)
    # we may need to create a function here to hold
    # another template in case elastic search does not load.

    res = es.search(index="test-rule1",
                    body={"query": {"match_all": {}}})

    # get the hits data from the search engine .. everything.
    hits = res[u'hits'][u'hits']
    
    # preapre the hits list and add questions into a list.
    # this list will handle all the questions.
    questionList = list()
    structList = list()
    
    for currentHit in hits:
        source = currentHit[u'_source']
        currentQuestion = source[u'Question']
        currentId = currentHit[u'_id']
        currentStruct = QuestionInfo( str(currentId), str(currentQuestion) );
        print >>sys.stderr, currentId
        questionList.append( str(currentQuestion) )
        structList.append( currentStruct )
        print >>sys.stderr, currentStruct

    # get the total number of results form the database.    
    total_hits = res[u'hits'][u'total']
    
    #print >>sys.stderr, total_hits;

    # this list holds the number of results and is passed to template
    results_list = [ total_hits ];
    
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': structList,
        'test_list': results_list
        })
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

#This is how get get rid of bloody csrf after you could't properly
#fix it after 1 hour of googleing... jesus
@csrf_exempt
def addContent( request ):
    # test and get the content of the questiona and answer from the previous page.
    template = loader.get_template('polls/content.html')

    if request.method == 'POST':
        element = request.POST.get("que", "" )
        ans = request.POST.get("ans", "" )
        print >>sys.stderr, 'Goodbye, cruel world!'
        print >>sys.stderr, element
        print >>sys.stderr, ans
        list = { "hello", element,}
        #list.append( ans )

        test_dict = {
        'Question': element,
            'Answer':ans
        }

        es = ES('http://127.0.0.1:9200/')
        res = es.index(index="test-rule1", doc_type='book', body=test_dict)
        print >>sys.stderr, res
        
        context = RequestContext(request, {
        'post_data': list,
        })
        return HttpResponse(template.render( context ) )
        
    # if a GET (or any other method) we'll create a blank form
    else:
        #return HttpResponse(template.render( request ) )
        return HttpResponse(template.render( "sorry brow" ) )
        #return render_to_response("polls/test.html", RequestContext(request, {}))

def renderQuestion( request, question_id ):
    template = loader.get_template('polls/test.html')
    response = "this is a test"
    #return HttpResponse( response )
    return HttpResponse(template.render())
    
