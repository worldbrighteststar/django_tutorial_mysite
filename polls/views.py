from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import loader

from .models import Question

# Create your views here.

def index(request):
    # 1st
    # lastest_question_list = Question.objects.order_by('-pub_date')[:5] # Question객체를 출판일 오름차순으로 앞에서 5개 가져옴
    # output = ', '.join([q.question_text for q in lastest_question_list])
    # return HttpResponse(output)

    # 2nd : template 사용
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = { # template에 context 데이터들을 전달 {template변수명 : python 객체}
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # 3rd : shortcuts 단축 기능 사용
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # 1 : try except 사용
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question: question'})

    # 2 : Django 단축기능 사용
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    respones = "You're looking at the results of question %s."
    return HttpResponse(respones % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)

