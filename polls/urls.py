from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
    # ex: /test/
    # Dont add the leading / from your test url. You should also add a ^ at the beginning of the regex, so that it matches test but not xtest.
    url('^test/$', views.test, name='test'),
    ]
