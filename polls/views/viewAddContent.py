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

@csrf_exempt
def addContent( request ):
    # Get the content of the question and answer from the previous page.
    template = loader.get_template('polls/content.html')

    if request.method == 'POST':
        element = request.POST.get("que", "" )
        ans = request.POST.get("ans", "" )
        list = { element, ans }

        test_dict = {
            'Question': element,
            'Answer':ans
        }

        es = ES('http://127.0.0.1:9200/')
        res = es.index(index="test-rule1", doc_type='book', body=test_dict)
        #check if res has something.
        context = RequestContext(request, {
            'post_data': list,
        })
        return HttpResponse(template.render( context ) )
        
    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponse(template.render( "sorry brow, can't add" ) )
