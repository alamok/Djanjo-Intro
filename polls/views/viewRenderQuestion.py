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

class QueWithAns:
    def __init__( self, que, ans, id ):
        self.queText = que
        self.ansText = ans
        self.id = id


def renderQuestion( request, id ):
    #get the response using id and search for the question
    es = ES('http://127.0.0.1:9200/')
    
    # There is bug here if no result is found.
    res = es.search( index="test-rule1",
        body = {
        "query": {
            "match": {
                "_id" : id
            }
        }
    } )
    
    # get the hits data from the search engine for the ID.
    hits = res[u'hits'][u'hits']
    
    source = hits[0][u'_source']
    currentQuestion = source[u'Question']
    currentAnswer = source[u'Answer']
     
    currentStruct = QueWithAns( str(currentQuestion), str(currentAnswer), id )

    template = loader.get_template('polls/qanda.html')
    context = RequestContext( request, {
        'qus_ans_pair': currentStruct
    } )
    
    return HttpResponse(template.render(context))    
