from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class QuestionCreateView(CreateView):
    model = Question
    template_name = "question/question_form.html"
    fields = ['name', 'email', 'tell_me_more']
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(QuestionCreateView, self).form_valid(form)
    
class Success(TemplateView):
    template_name = "success.html"
    


