from django.shortcuts import render, get_object_or_404, redirect
from ..models import Poll, Choice, Answer
from ..forms import AnswerForm
from django.views.generic.edit import FormMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView


class AnswerAddView(CreateView):
    template_name = 'answer/result_page.html'
    form_class = AnswerForm
    model = Answer

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        poll = Poll.objects.get(id=self.kwargs.get('pk'))
        print('hgjhgfg',poll)
        return form_class(poll, **self.get_form_kwargs())

    def form_valid(self, form):
        poll = get_object_or_404(Poll, id=self.kwargs.get('pk'))
        form.instance.poll = poll

        return redirect('index')

    def form_invalid(self, form):
        context = {'form': form}
        return render(self.request, self.template_name, context)

    def get_success_url(self):
        return reverse('index')


