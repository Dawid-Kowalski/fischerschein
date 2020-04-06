from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('question.urls', namespace='question')),
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
]
