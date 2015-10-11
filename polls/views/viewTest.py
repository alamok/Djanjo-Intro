#        DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#                    Version 2, December 2004 
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 

# Everyone is permitted to copy and distribute verbatim or modified 
# copies of this license document, and changing it is allowed as long 
# as the name is changed. 

# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 
# 0. You just DO WHAT THE FUCK YOU WANT TO.

from django.template import loader
from django.http import HttpResponse

# Not used anywhere just to standardise the work.
def test( request ):
    template = loader.get_template('polls/test.html')
    return HttpResponse(template.render()) 
