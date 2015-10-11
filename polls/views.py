
# Create your views here.

from django.http import HttpResponse
#This is how get get rid of bloody csrf after you could't properly
#fix it after 1 hour of googleing... jesus
class QuestionInfo:
    def __init__( self, id, text ):
        self.questionId = id
        self.questionText = text;

class QueWithAns:
    def __init__( self, que, ans ):
        self.queText = que
        self.ansText = ans;

def detail(request, question_id):
    return HttpResponse("you are looking at the results of question %s" % question_id)

def results(request, question_id):
    response = "you are looking at the results of question %s"
    return HttpResponse(response % question_id )

def vote(request, question_id):
    return HttpResponse("you are voting for the question %s." % question_id)
