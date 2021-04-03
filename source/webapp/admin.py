from django.contrib import admin
from .models import Poll, Choice, Answer

class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at']
    list_filter = ['question']
    search_fields = ['question']
    fields = ['id', 'question', 'created_at']
    readonly_fields = ['id']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'text']
    list_filter = ['text']
    search_fields = ['text']
    fields = ['id', 'poll', 'text']
    readonly_fields = ['id']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll_id', 'choice', 'created_at']
    list_filter = ['poll_id']
    search_fields = ['poll_id']
    fields = ['id', 'poll_id', 'choice', 'created_at']
    readonly_fields = ['id']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
