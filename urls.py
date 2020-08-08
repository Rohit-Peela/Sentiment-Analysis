from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^process_word', views.process_word, name='process'),
    url(r'^feature/', views.feature, name='features'),
    url(r'^login/', views.login, name='login'),
    url(r'^$', views.registration, name='registration'), 
]
