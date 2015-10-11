#        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#                    Version 2, December 2004 
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

# Everyone is permitted to copy and distribute verbatim or modified 
# copies of this license document, and changing it is allowed as long 
# as the name is changed. 

# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 
# 0. You just DO WHAT THE FUCK YOU WANT TO.

from django.http import HttpResponse
from django.template import RequestContext, loader
from elasticsearch import Elasticsearch as ES
from django.views.decorators.csrf import csrf_exempt

import sys

class QuestionInfo:
    def __init__( self, id, text ):
        self.questionId = id
        self.questionText = text;
        
@csrf_exempt
def index(request):
    # test a elastic search connection and create index 
    # if index already exists dont do anything

    es = ES('http://127.0.0.1:9200/')
    es.indices.create(index='test-rule1', ignore=400)
    # we may need to create a function here to hold
    # another template in case elastic search does not load.

    currentPage = 0
    if request.method == 'POST':
        currentPage = request.POST.get("page", "" )
        #print >>sys.stderr, "currentPAge"
        
    fromCount = 0
    fromCount = int( currentPage ) * int( 10 );
    
    # There is bug here if no result is found.
    res = es.search( index="test-rule1",
                     body= {
                         "query": {"match_all": {} },
                         "from": fromCount
                     }
    )

    # get the hits data from the search engine .. everything.
    hits = res[u'hits'][u'hits']
    
    # preapre the hit list not the one that hitman makes
    # the one that talks about search and add questions into a list.
    # this list will handle all the questions.
    questionList = list()
    structList = list()
    
    for currentHit in hits:
        source = currentHit[u'_source']
        currentQuestion = source[u'Question']
        currentId = currentHit[u'_id']
        currentStruct = QuestionInfo( str(currentId), str(currentQuestion) );
        questionList.append( str(currentQuestion) )
        structList.append( currentStruct )
        
    # get the total number of results form the database.    
    total_hits = res[u'hits'][u'total']
    
    # this list holds the number of results and is passed to template
    results_list = [ total_hits ];
    total_pages = total_hits/10;

    page_list =[]
    for count in range(0,total_pages + 1):
        page_list.append(count)
    
    template = loader.get_template('polls/index.html')
    context = RequestContext( request, {
        'latest_question_list': structList,
        'test_list': results_list,
        'pages': page_list
        } )
    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse("you are looking at the results of question %s" % question_id)
