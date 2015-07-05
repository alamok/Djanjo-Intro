import datetime

from django.db import models
from django.utils import timezone

# create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publisthed')
    def __unicode__(self):
        return self.question_text
    def was_recent(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question) # tells django each choice is related to a single question
    chioce_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.chioce_text
