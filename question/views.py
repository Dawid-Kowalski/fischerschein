from django.shortcuts import render, get_object_or_404
from .models import Question
from django.utils.translation import gettext as _

def simple_question(request):
    all_questions = Question.objects.all()
    return render(request,'question/simple_question.html',{'all_questions':all_questions})

def simple_test(request):
    all_questions = Question.objects.all()
    return render(request,'question/simple_test.html',{'all_questions':all_questions})

def main_page(request):
    return render(request,'question/main_page.html')

def fischerschein_info(request):
    return render(request,'question/fischerschein_info.html')

def FAQ(request):
    return render(request,'question/FAQ.html')

def project_info(request):
    return render(request,'question/project_info.html')