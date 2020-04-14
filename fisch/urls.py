from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('',include('question.urls', namespace='question')),
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
]
