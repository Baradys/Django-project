from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView


class FeedBackView(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback/feedback.html', context={'form': form})  # Приходим на пустую ветку

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('done/')
        return render(request, 'feedback/feedback.html', context={'form': form})  # Приходим на пустую ветку


class FeedBackUpdateView(View):
    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'{id_feedback}')
        return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ListFeedBackView(ListView):
    template_name = 'feedback/link_feedback.html'
    model = Feedback
    context_object_name = 'feedbacks'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.filter(rating__gt=4)
        return filter_qs


class DetailFeedBack(TemplateView):
    template_name = 'feedback/detail_feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feedback = Feedback.objects.get(id=context['id_feedback'])
        context['feedback'] = feedback
        return context
