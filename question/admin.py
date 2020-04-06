from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id','main_topic_ger','under_topic_ger','question_ger')
    list_filter = ('main_topic_ger','under_topic_ger')
    search_fields = ('main_topic_ger', 'main_topic_pl', 'under_topic_ger', 'under_topic_pl', 'question_ger', 'question_pl', 'answer_a_ger', 'answer_a_pl', 'answer_b_ger', 'answer_b_pl', 'answer_c_ger', 'answer_c_pl')
    ordering = ('question_id',)
