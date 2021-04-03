from django.shortcuts import render, get_object_or_404, redirect
from ..models import Poll, Choice
from ..forms import SimpleSearchForm, PollForm, ChoiceForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode
from django.http import HttpResponseRedirect


class ChoiceCreateView(CreateView):
    form_class = ChoiceForm
    model = Choice

    def get_success_url(self):
        return reverse(
            'poll',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        poll = get_object_or_404(Poll, id=self.kwargs.get('pk'))
        form.instance.poll = poll
        return super().form_valid(form)

class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/choice_update_view.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll', kwargs={'pk': self.object.poll.pk})

class ChoiceDeleteView(DeleteView):
    model = Choice

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('poll', kwargs={'pk': self.object.poll.pk})