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

# #print >>sys.stderr, "currentPAge"

class QuestionInfo:
    def __init__( self, id, text ):
        self.questionId = id
        self.questionText = text;

@csrf_exempt
def search( request ):
    template = loader.get_template('polls/search.html')
    
    searchStr = ""
    Input = "_all"
    fromCount = 0

    # we need few things for good search.
    # search text, place to search, page .. get them.
    if request.GET['Input']:
        Input = request.GET['Input']
        
    if request.GET['stext']:
        searchStr = request.GET['stext']

    if request.GET['page']:
        fromCount = request.GET['page']

    if isinstance( fromCount, int ):
        fromCount = int( fromCount ) * int( 10 );
    

    lookUpIn = Input
    es = ES('http://127.0.0.1:9200/')
    es.indices.create(index='test-rule1', ignore=400)
    
    currentPage = 0
    if request.method == 'POST':
        currentPage = request.POST.get("s_page", "" )
        
    fromCount = 0
    if isinstance( currentPage, int ):
        fromCount = int( currentPage ) * int( 10 );
    
    # There is bug here if no result is found.
    res = es.search( index="test-rule1", body= {
        "query": {
            "match": {
                lookUpIn : searchStr
            },
        },
        "from": fromCount
    } )
    
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
        questionList.append( str(currentQuestion) )
        structList.append( currentStruct )

    # get the total number of results form the database.    
    total_hits = res[u'hits'][u'total']

    # this list holds the number of results and is passed to template
    results_list = [ total_hits ];
    
    template = loader.get_template('polls/search.html')

    results_list = [ total_hits ];
    total_pages = total_hits/10;

    page_list =[]
    for count in range(0,total_pages + 1):
        page_list.append(count)
    
    context = RequestContext( request, {
        'latest_question_list': structList,
        'test_list': results_list,
        'pages': page_list,
        's_str': searchStr,
        'i_type': Input
        } )
    return HttpResponse(template.render(context))
