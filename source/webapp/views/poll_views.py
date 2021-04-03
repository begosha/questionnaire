from django.shortcuts import render, get_object_or_404, redirect
from ..models import Poll, Choice
from ..forms import SimpleSearchForm, PollForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode
from django.http import HttpResponseRedirect


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(question__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

class PollView(DetailView):
    model = Poll
    template_name = 'poll/poll_view.html'

class PollAddView(CreateView):
    template_name = 'poll/poll_add_view.html'
    form_class = PollForm
    model = Poll

    def form_valid(self, form):
        poll = Poll()
        for key, value in form.cleaned_data.items():
            setattr(poll, key, value)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')

class PollUpdateView(UpdateView):
    form_class = PollForm
    model = Poll
    template_name = 'poll/poll_update_view.html'
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll', kwargs={'pk': self.kwargs.get('pk')})

