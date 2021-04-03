from django import forms
from .models import Poll, Choice, Answer

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('question',)

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('text',)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('choice',)

    def __init__(self, poll, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = poll.master_poll.all()


