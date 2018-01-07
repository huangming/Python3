from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404, render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def ind(request):
    template = loader.get_template('polls/ind.html')
    
    #rendering the template in HttpResponse
    return HttpResponse(template.render())
	
#class ind(TemplateView):
#	template_name = 'polls/index.html'
