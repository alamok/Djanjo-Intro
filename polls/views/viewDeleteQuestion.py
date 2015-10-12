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

def deleteQuestion( request, id ):
    #get the response using id and search for the question
    es = ES('http://127.0.0.1:9200/')
    
    es.delete( index="test-rule1", doc_type="book", id=id )
    
    template = loader.get_template('polls/qdelete.html')
    context = RequestContext( request )
    
    return HttpResponse(template.render(context))    
