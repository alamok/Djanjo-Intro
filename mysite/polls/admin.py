from django.contrib import admin

from .models import Choice, Question

# Register your models here.

#Default
#admin.site.register(Question)

# 1st view change
#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_recent' )
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
