from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from .models import (
    Question,
    Choice,
)

# Create your views here.

def home_v1(request):
    question_list = Question.objects.order_by('-created_at')
    output = '<br><br> '.join([q.question for q in question_list])
    return HttpResponse(output)

def home_v2(request):
    template = loader.get_template('index.html')
    question_list = Question.objects.all()
    context={'question_list': question_list}
    return HttpResponse(template.render(context, request))

def home_v3(request):
    template_name = 'index.html'
    context={'question_list': Question.objects.all()}
    return render(request, template_name, context)


def detail_v1(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(request, "requested object doesnt exist")
    question_choices = ''.join(question.question+"<br>")
    question_choices += '<br>'.join([choice.choice_text for choice in question.question_choice.all()])
    return HttpResponse(question_choices)

def detail_v2(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(request, "requested object doesnt exist")
    
    template = loader.get_template('detail.html')
    context = {'question': question}
    return HttpResponse(template.render(context, request))

def detail_v3(request, question_id):
    template_name = 'detail.html'

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(request, "requested object doesnt exist")
    
    context = {'question': question, 'message':'success'}
    return render(request, template_name, context)


def vote_v1(request, question_id):
    return HttpResponse("Question vote %s" % question_id)

def vote_v2(request, question_id):
    return HttpResponse("Question vote %s" % question_id)

def vote_v3(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    try:
        choice = question.question_choice.get(id=request.POST.get('choice'))
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question': question, 'error_message': 'You don\'t select a choice'})
    else:
        choice.vote += 1
        choice.save()
        return HttpResponseRedirect(reverse('poll:result_v3', args=(question.pk,)))


def result_v1(request, question_id):
    response = "Question result %s"
    return HttpResponse(response % question_id)

def result_v2(request, question_id):
    response = "Question result %s"
    return HttpResponse(response % question_id)

def result_v3(request, question_id):
    template_name='result.html'
    question = get_object_or_404(Question, id=question_id)
    context={'question': question}
    return render(request, template_name, context)