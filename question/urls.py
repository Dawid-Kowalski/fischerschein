from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('simple_question',views.simple_question,name='simple_question'),
    path('simple_test',views.simple_test,name='simple_test'),
    path('fischerschein_info',views.fischerschein_info,name='fischerschein_info'),
    path('FAQ',views.FAQ,name='FAQ'),
    path('project_info',views.project_info,name='project_info'),
    path('',views.main_page,name='main_page'),
]