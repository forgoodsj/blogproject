__author__ = 'jun'
from django.conf.urls import url
from django.contrib import admin
from img import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'img'
urlpatterns = [
    url(r'^show', views.showImg, name='show'),
    url(r'^uploadpage', views.upload, name='uploadpage'),
    url(r'^done', views.Done, name='done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)